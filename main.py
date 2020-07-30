from github import Github
import re
import os
import shlex
import subprocess


def github_login(ACCESS_TOKEN, REPO_NAME):
    '''
    Use Pygithub to login to the repository

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
            pre = re.match(regex, commit[1]).group(0)
            scope = re.search(r'\(.+\)', pre).group(0)[1:-1]
            if scope.lower() == 'changelog' and regex == r'^docs\(.+\)':
                continue
            subject = re.sub(regex + r':', '', commit[1])
            if subject[0] == ' ':
                subject = subject[1:]
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
    for i in range(len(output)):
        tmp = []
        tmp.append(output[i][0:40])
        tmp.append(output[i][41:])
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
        processed_release.append(release.body)
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
        section = section + scope_content
    section = section + '\n'
    return section


def generate_changelog(repo, parsed_releases, feat, fix, docs, chore, refactor,
                       perf):
    '''
    Generate CHANGELOG

    Args:
        repo (github.Repository.Repository): object represents the repo
        parsed_releases (list): releases' information
        feat (string): set to 1 to generate it
        fix (string): set to 1 to generate it
        docs (string): set to 1 to generate it
        chore (string): set to 1 to generate it
        refactor (string): set to 1 to generate it
        perf (string): set to 1 to generate it

    Returns:
        string: content of CHANGELOG
    '''
    tags = get_tags()
    info_list = []
    CHANGELOG = '# CHANGELOG\n\n'
    feat_regex = r'^feat\(.+\)'
    fix_regex = r'^fix\(.+\)'
    docs_regex = r'^docs\(.+\)'
    chore_regex = r'^chore\(.+\)'
    refactor_regex = r'^refactor\(.+\)'
    perf_regex = r'^perf\(.+\)'
    for i in range(len(tags)):
        release_info = ''
        if i == 0:
            commit_list = get_commit_log_between_versions(tags[i], tags[i], 0)
        else:
            commit_list = get_commit_log_between_versions(
                tags[i - 1], tags[i], 1)
        if tags[i] == 'HEAD':
            title = 'Unreleased'
            description = 'Changes unreleased'
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
        if feat == 1:
            sec = generate_section(commit_list, feat_regex, repo)
            if sec != '\n':
                release_info = release_info + '### Features\n\n' + sec
        if fix == 1:
            sec = generate_section(commit_list, fix_regex, repo)
            if sec != '\n':
                release_info = release_info + '### Bug Fixes\n\n' + sec
        if docs == 1:
            sec = generate_section(commit_list, docs_regex, repo)
            if sec != '\n':
                release_info = release_info + '### Documentation Changes\n\n' + sec
        if chore == 1:
            sec = generate_section(commit_list, chore_regex, repo)
            if sec != '\n':
                release_info = release_info + '### Chores\n\n' + sec
        if refactor == 1:
            sec = generate_section(commit_list, refactor_regex, repo)
            if sec != '\n':
                release_info = release_info + '### Refactors\n\n' + sec
        if perf == 1:
            sec = generate_section(commit_list, perf_regex, repo)
            if sec != '\n':
                release_info = release_info + '### Performance Improvements\n\n' + sec
        info_list.append(release_info)
    for j in reversed(info_list):
        CHANGELOG = CHANGELOG + j
    CHANGELOG = CHANGELOG + '\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*'
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
    text = changelog
    repo.update_file(contents.path, commit_message, text, contents.sha)


def main():
    ACCESS_TOKEN = get_inputs('ACCESS_TOKEN')
    REPO_NAME = get_inputs('REPO_NAME')
    PATH = get_inputs('PATH')
    COMMIT_MESSAGE = get_inputs('COMMIT_MESSAGE')
    FEAT = int(get_inputs('FEAT'))
    FIX = int(get_inputs('FIX'))
    DOCS = int(get_inputs('DOCS'))
    CHORE = int(get_inputs('CHORE'))
    REFACTOR = int(get_inputs('REFACTOR'))
    PERF = int(get_inputs('PERF'))

    repo = github_login(ACCESS_TOKEN, REPO_NAME)
    parsed_releases = parse_releases(repo)
    CHANGELOG = generate_changelog(repo, parsed_releases, FEAT, FIX, DOCS,
                                   CHORE, REFACTOR, PERF)
    write_changelog(repo, CHANGELOG, PATH, COMMIT_MESSAGE)


if __name__ == '__main__':
    main()
