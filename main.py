#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-08-06 10:48:37
# @LastEditTime : 2021-01-16 12:36:45
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


def set_local_env(env_name, env_value, prefix='INPUT'):
    '''
    set local env for dev

    Args:
        env_name (str): local env name
        env_value (str): value of local env name
    '''
    os.environ[prefix + '_{}'.format(env_name).upper()] = env_value


def get_inputs(input_name):
    '''
    Get a Github actions input by name

    Args:
        input_name (str): input_name in workflow file

    Returns:
        string: action_input

    References
    ----------
    [1] https://help.github.com/en/actions/automating-your-workflow-with-github-actions/metadata-syntax-for-github-actions#example
    '''
    return os.getenv('INPUT_{}'.format(input_name).upper())


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
        'REPO_NAME', 'ACCESS_TOKEN', 'PATH', 'COMMIT_MESSAGE', 'TYPE'
    ]
    for param in option_params:
        if param not in params.keys():
            if args.token:
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
        else:
            tmp = params[param]
        set_local_env(param, tmp, prefix)


class GithubChangelog:
    '''
    Class for data interface of Github

    Use it to get changelog data and file content from Github and write new file content to Github
    '''
    def __init__(self, ACCESS_TOKEN, REPO_NAME, PATH, BRANCH, COMMIT_MESSAGE):
        '''
        Initial GithubContributors

        Args:
            ACCESS_TOKEN (str): Personal Access Token for Github
            REPO_NAME (str): The name of the repository
            PATH (str): The path to the file
            BRANCH (str): The branch of the file
            COMMIT_MESSAGE (str): Commit message you want to use
        '''
        self.COMMIT_MESSAGE = COMMIT_MESSAGE
        self.PATH = PATH
        self.BRANCH = BRANCH
        self.SHA = ''
        self.releases = {}
        self.changelog = ''
        # Use PyGithub to login to the repository
        # References: https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
        g = github.Github(ACCESS_TOKEN)
        self.repo = g.get_repo(REPO_NAME)

    def get_data(self):
        # get release info
        releases = self.repo.get_releases()
        self.releases['Unreleased'] = {'html_url': '', 'body': '', 'created_at': '', 'commit_sha': ''}
        for release in releases:
            self.releases[release.tag_name] = {'html_url': release.html_url, 'body': re.sub(r'\r\n', r'\n', release.body), 'created_at': release.created_at}
        # get tags and commits
        tags = self.repo.get_tags()
        for tag in tags:
            if tag.name in self.releases:
                self.releases[tag.name]['commit_sha'] = tag.commit.sha
        release_tags = list(self.releases.keys())[::-1]
        seq = 0
        commits = self.repo.get_commits(sha=self.BRANCH).reversed
        selected_commits = []
        pbar = tqdm(desc='Commits progress', total=commits.totalCount)
        for commit in commits:
            message = commit.commit.message.split('\n\n')
            message_head = message[0]
            if message_head[-3:] == '...' and len(message) > 1:
                if message[1][0:3] == '...':
                    message_head = re.sub(r'  ', r' ', message_head[:-3] + ' ' + message[1].split('\n')[0][3:])
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
            if commit.sha == self.releases[release_tags[seq]]['commit_sha']:
                self.releases[release_tags[seq]]['commits'] = selected_commits[::-1]
                selected_commits = []
                seq = seq + 1
            pbar.update(1)
        pbar.close()
        self.releases[release_tags[seq]]['commits'] = selected_commits[::-1]
        # get file content
        contents = self.repo.get_contents(self.PATH, self.BRANCH)
        self.PATH = contents.path
        self.SHA = contents.sha
        base = contents.content
        base = base.replace('\n', '')
        self.changelog = base64.b64decode(base).decode('utf-8')

    def read_releases(self):
        return self.releases

    def write_data(self, changelog):
        if changelog == self.changelog:
            pass
        else:
            self.repo.update_file(self.PATH, self.COMMIT_MESSAGE, changelog,
                                  self.SHA, self.BRANCH)


def strip_commits(commits, regex):
    '''
    Bypass some commits

    Args:
        commits (list): list of commit(dict), whose keys are 'head', 'sha', 'url', 'pr_links'
        regex (string): regex expression to match.

    Returns:
        dict: selected commits of every scope.
    '''
    scopes = {}
    for commit in commits:
        if re.match(regex, commit['head']):
            scope = re.findall(regex, commit['head'])[0]
            if scope.lower() == 'changelog' and regex == r'^docs[(](.+?)[)]':
                continue
            subject = re.sub(regex + r'\s?:\s?', '', commit['head'])
            if scope in scopes:
                scopes[scope].append({'subject': subject, 'commit': commit})
            else:
                scopes[scope] = []
                scopes[scope].append({'subject': subject, 'commit': commit})
    return scopes


def generate_section(release_commits, type_regex):
    '''
    Generate scopes of a section

    Args:
        release_commits (dict): commits of the release
        type_regex (string): regex expression

    Returns:
        string: content of section
    '''
    section = ''
    scopes = strip_commits(release_commits, type_regex)
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


def generate_release_body(release_commits, part_name):
    '''
    Generate release body using part_name_dict and regex_list

    Args:
        release_commits (dict): commits of the release
        part_name (list): a list of part_name, e.g. feat:Feature

    Returns:
        string: body part of release info
    '''
    release_body = ''
    for part in part_name:
        reg, name = part.split(':')
        regex = r'^'+ reg + r'[(](.+?)[)]'
        sec = generate_section(release_commits, regex)
        if sec != '':
            release_body = release_body + '### ' + name + '\n\n' + sec
    return release_body


def generate_changelog(releases, part_name):
    '''
    Generate CHANGELOG

    Args:
        releases: dict of release data
        part_name (list): a list of part_name, e.g. feat:Feature

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
            description = releases[release_tag]['body']
            date = releases[release_tag]['created_at']
            release_info = f'''## [{title}]({url}) - {date}\n\n{description}\n\n'''
        release_body = generate_release_body(release_commits, part_name)
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
    set_env_from_file('.github/workflows/changelog.yml', args)
    if args.mode == 'local':
        set_env_from_file('.github/workflows/changelog.yml', args)
    elif args.mode == 'github':
        pass
    else:
        print("Illegal mode option, please type \'-h\' to read the help")
        os.exit()
    ACCESS_TOKEN = get_inputs('ACCESS_TOKEN')
    REPO_NAME = get_inputs('REPO_NAME')
    PATH = get_inputs('PATH')
    COMMIT_MESSAGE = get_inputs('COMMIT_MESSAGE')
    if re.match(r'.*:.*', PATH):
        BRANCH = re.sub(r':.*', '', PATH)
        PATH = re.sub(r'.*:', '', PATH)
    else:
        BRANCH = github.GithubObject.NotSet
    part_name = re.split(r'\s?,\s?', get_inputs('TYPE'))
    changelog = GithubChangelog(ACCESS_TOKEN, REPO_NAME, PATH, BRANCH, COMMIT_MESSAGE)
    changelog.get_data()

    CHANGELOG = generate_changelog(changelog.read_releases(), part_name)

    if args.mode == 'local':
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(CHANGELOG)
    else:
        changelog.write_data(CHANGELOG)


if __name__ == '__main__':
    main()
