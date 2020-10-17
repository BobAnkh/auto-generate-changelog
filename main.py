#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-08-06 10:48:37
# @LastEditors  : BobAnkh
# @LastEditTime : 2020-10-16 00:21:45
# @FilePath     : /auto-generate-changelog/main.py
# @Description  : Main script of Github Action
# @Copyright 2020 BobAnkh

import os
import re
import shlex
import subprocess
import argparse

from github import Github


def github_login(ACCESS_TOKEN, REPO_NAME):
    '''
    Use PyGithub to login to the repository

    Args:
        ACCESS_TOKEN (string): github Access Token
        REPO_NAME (string): repository name

    Returns:
        github.Repository.Repository: object represents the repo

    References:
    ----------
    [1]https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
    '''
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo(REPO_NAME)
    return repo


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


def strip_commits(commits, regex):
    '''
    Bypass some commits

    Args:
        commits (list): list of commits that each element contains SHA and <head>
        regex (string): regex expression to match

    Returns:
        list: selected commits
        set: set of scopes
    '''
    output = []
    scope_set = []
    for commit in commits:
        if re.match(regex, commit[1]):
            scope = re.findall(regex, commit[1])[0]
            if scope.lower() == 'changelog' and regex == r'^docs[(](.+?)[)]':
                continue
            subject = re.sub(regex + r'\s?:\s?', '', commit[1])
            scope_set.append(scope)
            commit.append(scope)
            commit.append(subject)
            output.append(commit)
    return output, set(scope_set)


def get_tags():
    '''
    Get tags

    Returns:
        list of string: tag names including 'HEAD'
    '''
    command = 'git tag'
    output_bytes = subprocess.check_output(shlex.split(command),
                                           stderr=subprocess.STDOUT)
    output = output_bytes.decode('utf-8')
    output = output.split('\n')
    output[-1] = 'HEAD'
    return output


def get_commit_log_between_versions(previous_version, later_version, flag):
    '''
    Get the commit log between two versions

    Args:
        previous_version (string): previous version
        later_version (string): later version
        flag (int): set 1 to compare versions

    Returns:
        list of list: list of commit log(SHA + <head>) between versions
    '''
    if flag == 1:
        log_command = 'git log --pretty=format:"%H %s" ' + previous_version + '...' + later_version
    else:
        log_command = 'git log --pretty=format:"%H %s" ' + previous_version
    output_bytes = subprocess.check_output(shlex.split(log_command),
                                           stderr=subprocess.STDOUT)
    output = output_bytes.decode('utf-8')
    output = output.split('\n')
    output_list = []
    for item in output:
        tmp = []
        tmp.append(item[0:40])
        tmp.append(item[41:])
        output_list.append(tmp)
    return output_list


# def parse_commits(repo):
#     '''
#     Parse all commits

#     Args:
#         repo (github.Repository.Repository): object represents the repo

#     Returns:
#         list: each element contains a list which is the information of a commit

#     Ref:
#     commit_info: SHA, html_url, message, pull.number, pull.html_url
#     '''
#     parsed_commits = []
#     commits = repo.get_commits()
#     for commit in commits:
#         processed_commit = []
#         processed_commit.append(commit.sha)
#         processed_commit.append(commit.html_url)
#         processed_commit.append(commit.commit.message)
#         related_pulls = commit.get_pulls()
#         if related_pulls.totalCount == 0:
#             processed_commit.append([])
#         else:
#             pulls = []
#             for related_pull in related_pulls:
#                 pulls.append([related_pull.number, related_pull.html_url])
#             processed_commit.append(pulls)
#         parsed_commits.append(processed_commit)
#     return parsed_commits


def parse_releases(repo):
    '''
    Parse releases

    Args:
        repo (github.Repository.Repository): object represents the repo

    Returns:
        list: each element contains a list which is the information of a release

    Ref:
    release info: tag_name, html_url, body(description)
    '''
    parsed_releases = []
    releases = repo.get_releases()
    for release in releases:
        processed_release = []
        processed_release.append(release.tag_name)
        processed_release.append(release.html_url)
        release_body = re.sub(r'\r\n', r'\n', release.body)
        processed_release.append(release_body)
        processed_release.append(release.created_at)
        parsed_releases.append(processed_release)
    return parsed_releases


def generate_section(commit_list, type_regex, repo):
    '''
    Generate scopes of a section

    Args:
        commit_list (list): commits
        type_regex (string): regex expression
        repo (github.Repository.Repository): object represents the repo

    Returns:
        string: content of section
    '''
    section = ''
    sel_commits, scopes = strip_commits(commit_list, type_regex)
    for scope in scopes:
        scope_content = f'''- {scope}:\n'''
        for sel_commit in sel_commits:
            if sel_commit[2] == scope:
                commit = repo.get_commit(sel_commit[0])
                url = commit.html_url
                pulls = commit.get_pulls()
                prs = []
                if pulls.totalCount == 0:
                    pass
                else:
                    for pull in pulls:
                        pr = f''' ([#{pull.number}]({pull.html_url}))'''
                        prs.append(pr)
                scope_content = scope_content + f'''  - {sel_commit[3]} ([{sel_commit[0][0:7]}]({url}))'''
                for pr_link in prs:
                    scope_content = scope_content + pr_link
                scope_content = scope_content + '\n'
        section = section + scope_content + '\n'
    return section


def generate_release_body(commit_list, repo, part_name):
    '''
    Generate release body using part_name_dict and regex_list

    Args:
        commit_list (list): commits
        repo (github.Repository.Repository): object represents the repo
        part_name (list): a list of part_name, e.g. feat:Feature

    Returns:
        string: body part of release info
    '''
    release_body = ''
    for part in part_name:
        reg, name = part.split(':')
        regex = r'^' + reg + r'[(](.+?)[)]'
        sec = generate_section(commit_list, regex, repo)
        if sec != '':
            release_body = release_body + '### ' + name + '\n\n' + sec
    return release_body


def generate_changelog(repo, parsed_releases, part_name):
    '''
    Generate CHANGELOG

    Args:
        repo (github.Repository.Repository): object represents the repo
        parsed_releases (list): releases' information
        part_name (list): a list of part_name, e.g. feat:Feature

    Returns:
        string: content of CHANGELOG
    '''
    tags = get_tags()
    info_list = []
    CHANGELOG = '# CHANGELOG\n\n'
    for i, _ in enumerate(tags):
        release_info = ''
        if i == 0:
            commit_list = get_commit_log_between_versions(tags[i], tags[i], 0)
        else:
            commit_list = get_commit_log_between_versions(
                tags[i - 1], tags[i], 1)
        if tags[i] == 'HEAD':
            title = 'Unreleased'
            description = 'Changes unreleased.'
            release_info = f'''## {title}\n\n{description}\n\n'''
        else:
            for release in parsed_releases:
                if release[0] == tags[i]:
                    title = release[0]
                    url = release[1]
                    description = release[2]
                    date = release[3]
                    release_info = f'''## [{title}]({url}) - {date}\n\n{description}\n\n'''
                    break
        release_body = generate_release_body(commit_list, repo, part_name)
        if release_body == '' and tags[i] == 'HEAD':
            pass
        else:
            release_info = release_info + release_body
            info_list.append(release_info)
    for j in reversed(info_list):
        CHANGELOG = CHANGELOG + j
    CHANGELOG = CHANGELOG + r'\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*'
    CHANGELOG = CHANGELOG + '\n'
    return CHANGELOG


def write_changelog(repo, changelog, path, commit_message):
    '''
    Write contributors list to file if it differs

    Args:
        repo (github.Repository.Repository): object represents the repo
        changelog (string): content of changelog
        path (string): the file to write
        commit_message (string): commit message
    '''
    contents = repo.get_contents(path)
    repo.update_file(contents.path, commit_message, changelog, contents.sha)


def get_inputs_from_file(file_name, input_name):
    '''
    Read configuration from given local workflow file

    Args:
        file_name (string): the file to read from
        input_name (string): input_name in workflow file

    Returns:
        string: action_input
    '''
    file = open(file_name, 'r', encoding='utf-8')
    file_content = file.read().split('\n')
    file.close()
    target_flag = 0
    for _, line in enumerate(file_content):
        if target_flag == 0 and re.search('auto-generate-changelog@master',
                                          line):
            target_flag = 1
        if target_flag == 1 and re.search(input_name, line):
            return re.search("'(.*)'", line).group().strip('\'')
    return


def get_inputs_mode(arg, input_name):
    '''
    Choose proper place to get configuration when running locally or on github

    Args:
        arg (Namespace): place where parameters from cmd store
        input_name (str): input_name in workflow file

    Returns:
        string: action_input
    '''
    if arg.mode == 'local':
        return get_inputs_from_file(arg.file, input_name)
    elif arg.mode == 'github':
        return get_inputs(input_name)


def argument_parser():
    '''
    Parse parameters conveyed from cmd

    Returns:
        Namespace: place where parameters from cmd store
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mode",
        help="input local|github to choose to start locally or on github server",
        default="github")
    parser.add_argument(
        "-f",
        "--file",
        help="file to read configuration from when running local mode",
        default="./.github/workflows/changelog.yml")
    args = parser.parse_args()
    if args.mode not in ['local', 'github']:
        print("illegal input, please type \'-h\' to read the help")
        os.exit()
    return args


def main():
    args = argument_parser()
    ACCESS_TOKEN = get_inputs_mode(args, 'ACCESS_TOKEN')
    REPO_NAME = get_inputs_mode(args, 'REPO_NAME')
    PATH = get_inputs_mode(args, 'PATH')
    COMMIT_MESSAGE = get_inputs_mode(args, 'COMMIT_MESSAGE')
    part_name = get_inputs_mode(args, 'TYPE').split(',')
    repo = github_login(ACCESS_TOKEN, REPO_NAME)
    parsed_releases = parse_releases(repo)
    CHANGELOG = generate_changelog(repo, parsed_releases, part_name)


if __name__ == '__main__':
    main()
