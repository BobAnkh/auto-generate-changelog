#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-08-05 23:12:39
# @LastEditTime : 2021-01-11 16:25:37
# @Description  : Tests for main.py
# @Copyright 2020 BobAnkh

import json
import os
import random
import string
import sys

import pytest

sys.path.append('.')
import main

case = json.load(open('tests/case.json'))


@pytest.fixture(params=case['test_env_case'])
def generate_env(request):
    output = {}
    output['env_name'] = request.param
    output['env_value'] = ''.join(
        random.sample(string.ascii_letters + string.digits, 20))
    return output


def test_env(generate_env):
    env_name = generate_env['env_name']
    env_value = generate_env['env_value']
    main.set_local_env(env_name, env_value)
    msg = "Test case %s is wrong" % (env_name)
    assert env_value == main.get_inputs(env_name), msg

def test_get_tags():
    result = os.popen('git tag').read()
    result = result.split('\n')
    result[-1] = 'HEAD'
    assert result == main.get_tags()


@pytest.mark.parametrize("previous_version, later_version, flag, result", case['test_get_commit_log_between_versions_case'])
def test_get_commit_log_between_versions(previous_version, later_version,
                                         flag, result):
    assert result == main.get_commit_log_between_versions(previous_version, later_version, flag)


@pytest.mark.parametrize("commits, regex, output, sets", case['test_strip_commits_case'])
def test_strip_commits(commits, regex, output, sets):
    assert output, set(sets) == main.strip_commits(commits, regex)
