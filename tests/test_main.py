#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-08-05 23:12:39
# @LastEditTime : 2021-12-29 09:17:01
# @Description  : Tests for main.py
# @Copyright 2020 BobAnkh

import datetime
import json
# import os
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


@pytest.mark.parametrize("commits, regex, scopes", case['test_strip_commits'])
def test_strip_commits(commits, regex, scopes):
    assert scopes == main.strip_commits(commits, regex, "general", False)


@pytest.mark.parametrize("release_commits, type_regex, sec", case['test_generate_section'])
def test_generate_section(release_commits, type_regex, sec):
    assert sec == main.generate_section(release_commits, type_regex, "general", False)


@pytest.mark.parametrize("release_commits, part_name, release_body", case['test_generate_release_body'])
def test_generate_release_body(release_commits, part_name, release_body):
    assert release_body == main.generate_release_body(release_commits, part_name, "general", False)


@pytest.mark.parametrize("releases, part_name, changelog", case['test_generate_changelog'])
def generate_changelog(releases, part_name, changelog):
    for release in releases:
        releases[release]['created_at'] = datetime.datetime(2000, 1, 2, 3, 4, 5)
    assert changelog == main.generate_changelog(releases, part_name, "general", False)
