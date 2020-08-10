#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-08-05 23:12:39
# @LastEditors  : BobAnkh
# @LastEditTime : 2020-08-10 14:55:27
# @FilePath     : /auto-generate-changelog/tests/test_main.py
# @Description  : Tests for main.py
# @Copyright 2020 BobAnkh

import os
import sys

import pytest

sys.path.append('.')
import main


def test_get_tags():
    result = os.popen('git tag').read()
    result = result.split('\n')
    result[-1] = 'HEAD'
    assert result == main.get_tags()


@pytest.mark.parametrize("commits, regex, output, set", [
    ([[1, 'docs(changelog): fix a typo'], [2, 'feat(README): add it']
      ], r'^feat[(](.+?)[)]', [[2, 'feat(README): add it', 'README', 'add it']
                               ], {'README'}),
    ([[1, 'docs(*): add contributing guideline'],
      [2, 'feat(changelog): change function']], r'^docs[(](.+?)[)]', [[
          1, 'docs(*): add contributing guideline', '*',
          'add contributing guideline'
      ]], {'*'}),
    ([[1, 'docs(*): add contributing guideline'],
      [2, 'docs(changelog): fix a typo']], r'^docs[(](.+?)[)]', [[
          1, 'docs(*): add contributing guideline', '*',
          'add contributing guideline'
      ]], {'*'}),
    ([[1, 'feat(*): add contributing guideline'],
      [2, 'feat(changelog): change function']], r'^feat[(](.+?)[)]', [[
          1, 'feat(*): add contributing guideline', '*',
          'add contributing guideline'
      ], [
          2, 'feat(changelog): change function', 'changelog', 'change function'
      ]], {'changelog', '*'}),
])
def test_strip_commits(commits, regex, output, set):
    assert output, set == main.strip_commits(commits, regex)
