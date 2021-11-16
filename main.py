#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-08-06 10:48:37
# @LastEditTime : 2021-09-24 16:33:36
# @Description  : Main script of Github Action
# @Copyright 2020 BobAnkh

import argparse
import base64
import os
import re

import github
import yaml
from tqdm import tqdm


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--mode',
        help=
        'choose to use local-dev mode or on github action mode. Valid values are \'local\' or \'github\'',
        default='github')
    parser.add_argument(
        '-f',
        '--file',
        help='configuration file to read from when running local-dev mode',
        default='.github/workflows/changelog.yml')
    parser.add_argument('-o',
                        '--output',
                        help='output file when running local-dev mode',
                        default='local-dev.md')
    parser.add_argument('-t', '--token', help='Github Access Token')
    args = parser.parse_args()
    return args


def set_local_env(env_name: str, env_value: str, prefix='INPUT'):
    '''
    set local env for dev

    Args:
        env_name (str): local env name.
        env_value (str): value of local env name.
        prefix (str, optional): prefix of env variable. Defaults to 'INPUT'.
    '''
    os.environ[prefix + '_{}'.format(env_name).upper()] = env_value


def get_inputs(input_name: str, prefix='INPUT') -> str:
    '''
    Get a Github actions input by name

    Args:
        input_name (str): input_name in workflow file.
        prefix (str, optional): prefix of input variable. Defaults to 'INPUT'.

    Returns:
        str: action_input

    References
    ----------
    [1] https://help.github.com/en/actions/automating-your-workflow-with-github-actions/metadata-syntax-for-github-actions#example
    '''
    return os.getenv(prefix + '_{}'.format(input_name).upper())


def set_env_from_file(file, args, prefix='INPUT'):
    '''
    Set env when use local-dev mode

    Args:
        file (str): path to config file
        args (object): argument
        prefix (str, optional): prefix of env. Defaults to 'INPUT'.
    '''
    f = open(file, encoding='utf-8')
    y = yaml.safe_load(f)
    for job in y['jobs'].values():
        for step in job['steps']:
            if re.match(r'BobAnkh/auto-generate-changelog', step['uses']):
                params = step['with']
                break
    option_params = [
        'REPO_NAME', 'ACCESS_TOKEN', 'PATH', 'COMMIT_MESSAGE', 'TYPE', 'COMMITTER', 'DEFAULT_SCOPE', 'SUPPRESS_UNSCOPED'
    ]
    for param in option_params:
        if param not in params.keys():
            if param == 'ACCESS_TOKEN' and args.token:
                tmp = args.token
            else:
                tmp = input('Please input the value of ' + param + ':')
        elif param == 'ACCESS_TOKEN':
            if re.match(r'\$\{\{secrets\.', params[param]):
                if args.token:
                    tmp = args.token
                else:
                    tmp = input('Please input the value of ' + param + ':')
            else:
                tmp = params[param]
        elif param == 'REPO_NAME' and params[param] == '':
            tmp = input('Please input the value of ' + param + ':')
        else:
            tmp = params[param]
        set_local_env(param, tmp, prefix)


class GithubChangelog:
    '''
    Class for data interface of Github

    Use it to get changelog data and file content from Github and write new file content to Github
    '''
    def __init__(self, ACCESS_TOKEN, REPO_NAME, PATH, BRANCH, PULL_REQUEST, COMMIT_MESSAGE, COMMITTER):
        '''
        Initial GithubContributors

        Args:
            ACCESS_TOKEN (str): Personal Access Token for Github
            REPO_NAME (str): The name of the repository
            PATH (str): The path to the file
            BRANCH (str): The branch of the file
            PULL_REQUEST (str): Pull request target branch, none means do not open a pull request
            COMMIT_MESSAGE (str): Commit message you want to use
            COMMITTER (str): Committer you want to use to commit the file
        '''
        self.__commit_message = COMMIT_MESSAGE
        self.__path = PATH
        self.__branch = BRANCH
        self.__pull_request = PULL_REQUEST
        self.__sha = ''
        self.__releases = {}
        self.__changelog = ''
        self.__file_exists = False
        # Use PyGithub to login to the repository
        # References: https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
        g = github.Github(ACCESS_TOKEN)
        self.__repo = g.get_repo(REPO_NAME)
        self.__author = github.GithubObject.NotSet if COMMITTER == '' else github.InputGitAuthor(COMMITTER.split(' ')[0], COMMITTER.split(' ')[1])

    def get_data(self):
        # get release info
        releases = self.__repo.get_releases()
        self.__releases['Unreleased'] = {'html_url': '', 'body': '', 'created_at': '', 'commit_sha': ''}
        for release in releases:
            self.__releases[release.tag_name] = {'html_url': release.html_url, 'body': re.sub(r'\r\n', r'\n', release.body), 'created_at': release.created_at}
        # get tags and commits
        tags = self.__repo.get_tags()
        for tag in tags:
            if tag.name in self.__releases:
                self.__releases[tag.name]['commit_sha'] = tag.commit.sha
        release_commit_sha_list = {self.__releases[x]['commit_sha']:x for x in self.__releases}
        release_tags = list(self.__releases.keys())[::-1]
        seq = 0
        commits = self.__repo.get_commits(sha=self.__branch).reversed
        selected_commits = []
        pbar = tqdm(desc='Commits progress', total=commits.totalCount)
        for commit in commits:
            message = commit.commit.message.split('\n\n')
            message_head = message[0]
            if message_head[-3:] == '...' and len(message) > 1:
                if message[1][0:3] == '...':
                    message_head = re.sub(r'  ', r' ', message_head[:-3] + ' ' + message[1].split('\n')[0][3:])
            # TODO: #5 revert: remove from selected_commits
            url = commit.html_url
            pulls = commit.get_pulls()
            pr_links = []
            if pulls.totalCount == 0:
                pass
            else:
                for pull in pulls:
                    pr = f''' ([#{pull.number}]({pull.html_url}))'''
                    pr_links.append(pr)
            selected_commits.append({'head': message_head, 'sha': commit.sha, 'url': url, 'pr_links': pr_links})
            if commit.sha == self.__releases[release_tags[seq]]['commit_sha']:
                self.__releases[release_tags[seq]]['commits'] = selected_commits[::-1]
                selected_commits = []
                seq = seq + 1
            else:
                if commit.sha in release_commit_sha_list:
                    while (seq < release_tags.index(release_commit_sha_list[commit.sha])):
                        print(f'\n[DEBUG]Skip {release_tags[seq]} because the release commit is not in the log history')
                        self.__releases[release_tags[seq]]['commits'] = []
                        seq = seq + 1
                    if commit.sha == self.__releases[release_tags[seq]]['commit_sha']:
                        self.__releases[release_tags[seq]]['commits'] = selected_commits[::-1]
                        selected_commits = []
                        seq = seq + 1
            pbar.update(1)
        pbar.close()
        while (seq < len(release_tags) - 1):
            print(f'\n[DEBUG]Skip {release_tags[seq]} because the release commit is not in the log history')
            self.__releases[release_tags[seq]]['commits'] = []
            seq = seq + 1
        self.__releases[release_tags[seq]]['commits'] = selected_commits[::-1]
        # get file content
        try:
            contents = self.__repo.get_contents(self.__path, self.__branch)
        except github.GithubException as e:
            if e.status == 404:
                self.__changelog = ''
            else:
                raise github.GithubException(e.status, e.data)
        else:
            self.__file_exists = True
            self.__path = contents.path
            self.__sha = contents.sha
            base = contents.content
            base = base.replace('\n', '')
            self.__changelog = base64.b64decode(base).decode('utf-8')

    def read_releases(self):
        return self.__releases

    def write_data(self, changelog):
        if changelog == self.__changelog:
            pass
        else:
            if self.__file_exists:
                self.__repo.update_file(self.__path, self.__commit_message, changelog,
                                    self.__sha, self.__branch, self.__author)
            else:
                self.__repo.create_file(self.__path, self.__commit_message, changelog,
                                    self.__branch, self.__author)
            print(f'[DEBUG] BRANCH: {self.__branch}, PULL_REQUEST: {self.__pull_request}')
            if self.__pull_request != '' and self.__pull_request != self.__branch:
                self.repo.create_pull(title=self.__commit_message, body=self.__commit_message, base=self.__pull_request, head=self.__branch, draft=False, maintainer_can_modify=True)


def strip_commits(commits, type_regex, default_scope, suppress_unscoped):
    '''
    Bypass some commits

    Args:
        commits (list): list of commit(dict), whose keys are 'head', 'sha', 'url', 'pr_links'
        type_regex (string): regex expression to match.
        default_scope (str): scope which matches all un-scoped commits
        suppress_unscoped (bool): flag which suppresses entries for un-scoped commits

    Returns:
        dict: selected commits of every scope.
    '''
    # TODO: add an attribute to ignore scope 
    regex = r'^' + type_regex + r'(?:[(](.+?)[)])?'
    scopes = {}
    for commit in commits:
        head = commit['head']
        if re.match(regex, head):
            scope = re.findall(regex, head)[0]
            if scope == '':
                if suppress_unscoped:
                    continue
                scope = default_scope
            if scope.lower() == 'changelog' and regex == r'^docs(?:[(](.+?)[)])?':
                continue
            subject = re.sub(regex + r'\s?:\s?', '', head)
            if scope in scopes:
                scopes[scope].append({'subject': subject, 'commit': commit})
            else:
                scopes[scope] = []
                scopes[scope].append({'subject': subject, 'commit': commit})
    return scopes


def generate_section(release_commits, regex, default_scope, suppress_unscoped):
    '''
    Generate scopes of a section

    Args:
        release_commits (dict): commits of the release
        regex (string): regex expression
        default_scope (str): scope which matches all un-scoped commits
        suppress_unscoped (bool): flag which suppresses entries for un-scoped commits

    Returns:
        string: content of section
    '''
    section = ''
    scopes = strip_commits(release_commits, regex, default_scope, suppress_unscoped)
    for scope in scopes:
        scope_content = f'''- {scope}:\n'''
        for sel_commit in scopes[scope]:
            commit = sel_commit['commit']
            sha = commit['sha']
            url = commit['url']
            subject = sel_commit['subject']
            pr_links = commit['pr_links']
            scope_content = scope_content + f'''  - {subject} ([{sha[0:7]}]({url}))'''
            for pr_link in pr_links:
                scope_content = scope_content + pr_link
            scope_content = scope_content + '\n'
        section = section + scope_content + '\n'
    return section


def generate_release_body(release_commits, part_name, default_scope, suppress_unscoped):
    '''
    Generate release body using part_name_dict and regex_list

    Args:
        release_commits (dict): commits of the release
        part_name (list): a list of part_name, e.g. feat:Feature
        default_scope (str): scope which matches all un-scoped commits
        suppress_unscoped (bool): flag which suppresses entries for un-scoped commits

    Returns:
        string: body part of release info
    '''
    release_body = ''
    # TODO: add a new attribute to ignore some commits with another new function
    for part in part_name:
        regex, name = part.split(':')
        sec = generate_section(release_commits, regex, default_scope, suppress_unscoped)
        if sec != '':
            release_body = release_body + '### ' + name + '\n\n' + sec
    return release_body


def generate_changelog(releases, part_name, default_scope, suppress_unscoped):
    '''
    Generate CHANGELOG

    Args:
        releases: dict of release data
        part_name (list): a list of part_name, e.g. feat:Feature
        default_scope (str): scope which matches all un-scoped commits
        suppress_unscoped (bool): flag which suppresses entries for un-scoped commits

    Returns:
        string: content of CHANGELOG
    '''
    info_list = []
    CHANGELOG = '# CHANGELOG\n\n'
    for release_tag in releases:
        release_info = ''
        release_commits = releases[release_tag]['commits']
        if release_tag == 'Unreleased':
            title = 'Unreleased'
            description = 'Changes unreleased.'
            release_info = f'''## {title}\n\n{description}\n\n'''
        else:
            title = release_tag
            url = releases[release_tag]['html_url']
            origin_desc = re.split(r'<!-- HIDE IN CHANGELOG BEGIN -->(?:.|\n)*?<!-- HIDE IN CHANGELOG END -->', releases[release_tag]['body'])
            if len(origin_desc) == 1:
                description = origin_desc[0]
            else:
                description = ''
                for elem in origin_desc:
                    if elem == origin_desc[0]:
                        para = re.sub(r'\n*$', r'', elem)
                        description = description + para
                    elif elem == origin_desc[-1]:
                        para = re.sub(r'^\n*', r'', elem)
                        if para == '':
                            continue
                        elif description == '':
                            description = description + para
                        else:
                            description = description + '\n\n' + para
                    else:
                        para = re.sub(r'\n*$', r'', elem)
                        para = re.sub(r'^\n*', r'', para)
                        if para == '':
                            continue
                        elif description == '':
                            description = description + para
                        else:
                            description = description + '\n\n' + para
            date = releases[release_tag]['created_at']
            if description == '':
                description = '*No description*'
            release_info = f'''## [{title}]({url}) - {date}\n\n{description}\n\n'''
        release_body = generate_release_body(release_commits, part_name, default_scope, suppress_unscoped)
        if release_body == '' and release_tag == 'Unreleased':
            continue
        else:
            release_info = release_info + release_body
            info_list.append(release_info)
    for j in info_list:
        CHANGELOG = CHANGELOG + j
    CHANGELOG = CHANGELOG + r'\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*'
    CHANGELOG = CHANGELOG + '\n'
    return CHANGELOG


def main():
    args = argument_parser()
    if args.mode == 'local':
        set_env_from_file(args.file, args)
    elif args.mode == 'github':
        pass
    else:
        print("Illegal mode option, please type \'-h\' to read the help")
        os.exit()
    ACCESS_TOKEN = get_inputs('ACCESS_TOKEN')
    REPO_NAME = get_inputs('REPO_NAME')
    if REPO_NAME == '':
        REPO_NAME = get_inputs('REPOSITORY', 'GITHUB')
    PATH = get_inputs('PATH')
    BRANCH = get_inputs('BRANCH')
    if BRANCH == '':
        BRANCH = github.GithubObject.NotSet
    PULL_REQUEST = get_inputs('PULL_REQUEST')
    COMMIT_MESSAGE = get_inputs('COMMIT_MESSAGE')
    COMMITTER = get_inputs('COMMITTER')
    part_name = re.split(r'\s?,\s?', get_inputs('TYPE'))
    DEFAULT_SCOPE = get_inputs('DEFAULT_SCOPE')
    SUPPRESS_UNSCOPED = get_inputs('SUPPRESS_UNSCOPED')
    changelog = GithubChangelog(ACCESS_TOKEN, REPO_NAME, PATH, BRANCH, PULL_REQUEST, COMMIT_MESSAGE, COMMITTER)
    changelog.get_data()

    CHANGELOG = generate_changelog(changelog.read_releases(), part_name, DEFAULT_SCOPE, SUPPRESS_UNSCOPED == 'true')

    if args.mode == 'local':
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(CHANGELOG)
    else:
        changelog.write_data(CHANGELOG)


if __name__ == '__main__':
    main()
