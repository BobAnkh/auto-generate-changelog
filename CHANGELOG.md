# CHANGELOG

## Unreleased

*No description*

### Feature

- main:
  - add logs ([f58349e](https://github.com/BobAnkh/auto-generate-changelog/commit/f58349e096c357bd8b5899a7003e11e4a8d5e4a5))

- incr:
  - add incr generate ([999e098](https://github.com/BobAnkh/auto-generate-changelog/commit/999e098a789dcd53463e02f20d8d5f02c37d433c))

### Bug Fixes

- release:
  - fix typo ([ecf8b65](https://github.com/BobAnkh/auto-generate-changelog/commit/ecf8b658a274957a45342708d61006ce98e5eb12))

### Documentation

- README:
  - update contributors ([483962f](https://github.com/BobAnkh/auto-generate-changelog/commit/483962fdf04219faa0e752dcd2ece4ee50291bb7))

## [v1.1.1](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.1.1) - 2021-12-29 11:35:12

Fix bug of opening pull request when file/branch not exist.

See #78 for more details

### Feature

- pr:
  - detect branch to create ([7432a63](https://github.com/BobAnkh/auto-generate-changelog/commit/7432a6350cc2ca628dc0d9c3addac7e81245ac06))
  - create pr before submit content ([ccf0820](https://github.com/BobAnkh/auto-generate-changelog/commit/ccf08204e598f60cbff9316fb703a8e2341a8d32))

### Bug Fixes

- pr:
  - add check before create ([4d502dd](https://github.com/BobAnkh/auto-generate-changelog/commit/4d502dddbbfcc12b7d22f8e9b92bb1d1c5ad0202))
  - log dbg msg if fail to create ([5f9a23a](https://github.com/BobAnkh/auto-generate-changelog/commit/5f9a23a856eef22ee4dc717e89e5c23800e84429))

- commit:
  - get default if branch not exist ([dcb039a](https://github.com/BobAnkh/auto-generate-changelog/commit/dcb039a2e51368f2307cc73b94e2620b12ca7f26))

- main:
  - resolve pull request create ([de73071](https://github.com/BobAnkh/auto-generate-changelog/commit/de73071728fbe374e1c16397d4175ea50d66afa8))

### Documentation

- readme:
  - update usage of new params ([330883d](https://github.com/BobAnkh/auto-generate-changelog/commit/330883d8992c5d681c096f74f723c4893659c829))

- README:
  - update contributors ([b47f62c](https://github.com/BobAnkh/auto-generate-changelog/commit/b47f62c83e1ad2bfcf456390e2343f81d65ebbc8))

### Refactor

- main:
  - add some debug msg ([6d51a1e](https://github.com/BobAnkh/auto-generate-changelog/commit/6d51a1ebf43e0b41c2101297c7b7077d667ad28d))

## [v1.1.0](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.1.0) - 2021-11-16 17:38:44

Fix the bug that unscoped commits will now be picked up by default and listed under the scope `general`, which is configured by the new param `DEFAULT_SCOPE`. And if you don't want any unscoped commits to show up in your changelog, you can set param `SUPPRESS_UNSCOPED` to true (default to false).

### Feature

- main:
  - add options to configure scope related behaviour (#75) ([d9d66d2](https://github.com/BobAnkh/auto-generate-changelog/commit/d9d66d2893adc3b342d018c65741d9aee56fc715)) ([#75](https://github.com/BobAnkh/auto-generate-changelog/pull/75))

## [v1.0.7](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.7) - 2021-09-25 02:36:00

New Feature:

- Split param `PATH` into `PATH` and `BRANCH`: you can specify which file path in `PATH` param and which branch to update changes in `BRANCH` param.
- Add new param `PULL_REQUEST`, which must be used together with param `BRANCH`. Default set to `''` means not to open a pull request. You can set a target branch name in `PULL_REQUEST` that is different with `BRANCH` so that to do the following things:
  - Commit changes(if have) to file specified in `PATH` in `BRANCH`(if not set means default branch)
  - If `PULL_REQUEST` set to a different branch with `BRANCH` then a new pull request will be opened.

### Feature

- pull:
  - add new param for pull request ([6e3017a](https://github.com/BobAnkh/auto-generate-changelog/commit/6e3017ada58806239009553a6cab8eb146bf0c40))

- param:
  - add repo detect and BRANCH option ([d7b7a99](https://github.com/BobAnkh/auto-generate-changelog/commit/d7b7a992110cd9454b29d4496f6b68b303a12e35))

### Bug Fixes

- pull:
  - resolve missing arguments ([adc6b0d](https://github.com/BobAnkh/auto-generate-changelog/commit/adc6b0d3a444ca2b19bb2ee863a9e2e7cf0e2282))

### Documentation

- readme:
  - update usage for new param ([16df1a0](https://github.com/BobAnkh/auto-generate-changelog/commit/16df1a0bae9972c7112738b6059540c5688481bd))
  - update usage for new param ([06a8569](https://github.com/BobAnkh/auto-generate-changelog/commit/06a8569a5d62765e94f300725cd38c6309ec1ff5))
  - update usage for params ([53f175c](https://github.com/BobAnkh/auto-generate-changelog/commit/53f175c06b93eb9c17b037293846175694083698))

- README:
  - update contributors ([89e0465](https://github.com/BobAnkh/auto-generate-changelog/commit/89e0465a8f694fd619022020fe9843392701877b))

## [v1.0.6](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.6) - 2021-08-18 02:51:28

Feature: Add new input param `COMMITTER` for user to specify the committer to update file. It should be in format like `author <author@example>`

### Feature

- changelog:
  - add new input param COMMITTER ([741e5f3](https://github.com/BobAnkh/auto-generate-changelog/commit/741e5f3f130283e749fea0526bed1c2c3cd7fcb4))
  - specify commiter ([61c0ba1](https://github.com/BobAnkh/auto-generate-changelog/commit/61c0ba1706d112abcab006f6ae404dce644bd4f7))

### Documentation

- README:
  - update usage for token ([4bcbaff](https://github.com/BobAnkh/auto-generate-changelog/commit/4bcbaff70b2325361036b9584bf43ed85cb832b5))

## [v1.0.5](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.5) - 2021-08-18 01:41:46

Bugfix: automatically detect git version used in docker build to avoid mismatching git version

### Feature

- dockerfile:
  - add auto-detect git version ([d13f31d](https://github.com/BobAnkh/auto-generate-changelog/commit/d13f31df06904cb98e7b9e2404052829a0b12df9))

## [v1.0.4](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.4) - 2021-07-16 10:37:12

Fix the problem of release tag commit not in the git log history with empty commits list given to the release. The corresponding section in CHANGELOG will be empty.

### Bug Fixes

- release:
  - exclude release commits not in git log history ([aed3b71](https://github.com/BobAnkh/auto-generate-changelog/commit/aed3b712c06c8781730fa3649fbf911bfcd40646))

### Documentation

- README:
  - update usage notes ([9ff51d8](https://github.com/BobAnkh/auto-generate-changelog/commit/9ff51d8cc9248538d75f622aa53d346c6dceca2c))
  - change the example ([6d20b11](https://github.com/BobAnkh/auto-generate-changelog/commit/6d20b1131256e313b7ef2842f38492daa2df7b64))

## [v1.0.3](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.3) - 2021-04-26 05:03:38

Performance improvement for Dockerfile.

### Feature

- changelog:
  - support to create new file ([812a532](https://github.com/BobAnkh/auto-generate-changelog/commit/812a532d569106083c9b2f73978f8e435b64bc02))

### Documentation

- README:
  - update notes ([16bcc94](https://github.com/BobAnkh/auto-generate-changelog/commit/16bcc944a555f4a1736e1f1c047e99132f074911))
  - update desc ([25451eb](https://github.com/BobAnkh/auto-generate-changelog/commit/25451eb5c449298e3d1d3ebe3ce919cc1438eb72))
  - add info for local mode and tests ([ce7ca61](https://github.com/BobAnkh/auto-generate-changelog/commit/ce7ca6149979df82b500bd0ce194127823ebc4dc))

### Performance Improvements

- Dockerfile:
  - merge layers ([b657899](https://github.com/BobAnkh/auto-generate-changelog/commit/b65789969c1e8dc686fdb75fdaf8173116f0cdae))

## [v1.0.2](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.2) - 2021-01-16 12:52:26

In this version:

- refactor the data structure
- support other branches
- can hide lines in release description

### Feature

- release_info:
  - hide lines in CHANGELOG ([4e37a8b](https://github.com/BobAnkh/auto-generate-changelog/commit/4e37a8b72daa64aa5aa088ac6336fa16dc7e094b)) ([#40](https://github.com/BobAnkh/auto-generate-changelog/pull/40))

- mode:
  - add local-dev mode and BRANCH option ([ed4a0c8](https://github.com/BobAnkh/auto-generate-changelog/commit/ed4a0c85bbcf7bf9b6e7b3354a1b21e4fec1f3a8)) ([#40](https://github.com/BobAnkh/auto-generate-changelog/pull/40))
  - add local-dev mode ([f8036c7](https://github.com/BobAnkh/auto-generate-changelog/commit/f8036c74ff5369f2ddca0b82cbc7eed87c279676))

- join:
  - join header and body if necessary ([ea31132](https://github.com/BobAnkh/auto-generate-changelog/commit/ea31132b67756e0a6341c7477e1b20afee0db4ef)) ([#25](https://github.com/BobAnkh/auto-generate-changelog/pull/25))

## [v1.0.1](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.1) - 2020-10-16 12:14:37

fix the bug of CRLF in release info

### Bug Fixes

- release_body:
  - replace CRLF with LF ([afa6acb](https://github.com/BobAnkh/auto-generate-changelog/commit/afa6acbb82fde7ff625b012f8e30b8999550f18e))

### Documentation

- README:
  - add a new badge ([38eaef5](https://github.com/BobAnkh/auto-generate-changelog/commit/38eaef54fcbf2bb481c0f1ae2c5e30d9da7ab030))

## [v1.0.0](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v1.0.0) - 2020-10-13 00:59:50

Major version changes with some inputs removed and a new flexible and scaleble input introduced.

TYPE is introduced for users to define what they want to detect and where they want to have it in CHANGELOG all by themselves. Users can define the keyword detected from commit message and the corresonding word presented in the changelog in input `TYPE`. For example, define `feat:Feature` will detect commit message like `feat(main): add new option` and present this in changelog as part `Feature`.

BREAKING CHANGE: FEAT,FIX,DOCS,CHORE,REFACTOR,PERF are removed.

### Feature

- type:
  - merge different types into one ([4361af2](https://github.com/BobAnkh/auto-generate-changelog/commit/4361af20b49889d5fed90c9b90834f414ec1b5a6)) ([#20](https://github.com/BobAnkh/auto-generate-changelog/pull/20))

### Bug Fixes

- unrelease:
  - remove empty unreleased part ([4920949](https://github.com/BobAnkh/auto-generate-changelog/commit/49209493745b74c14a988f6215ec8bdab0783b39))

### Documentation

- README:
  - update inputs for new version ([c2d4415](https://github.com/BobAnkh/auto-generate-changelog/commit/c2d4415e7e1840c57bf17eab72b56db2f6cac802))

- CONTRIBUTING:
  - update style guide ([1f67fb9](https://github.com/BobAnkh/auto-generate-changelog/commit/1f67fb9279ad39ec9aff7021b484343ccc2bd914))

## [v0.0.4](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v0.0.4) - 2020-09-05 12:03:11

This might be the last release for this major version. I'm going to refactor the code to give more flexibility to the users in the future.

### Feature

- general:
  - feature(main): add a newline to end of changelog ([e40fb49](https://github.com/BobAnkh/auto-generate-changelog/commit/e40fb4969d0b8d9f7ebc960bee346fee4474318b))

### Bug Fixes

- main:
  - add a blank newline at the end ([9ae5e55](https://github.com/BobAnkh/auto-generate-changelog/commit/9ae5e5526238ccc48337db1bc0b0f2958e588ab5))

### Performance Improvements

- main:
  - extract release_body generation ([e7f49c2](https://github.com/BobAnkh/auto-generate-changelog/commit/e7f49c2f1467ccd4cc2182cda7cc4ad569e05280))

## [v0.0.3](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v0.0.3) - 2020-08-10 08:02:40

See [CHANGELOG](https://github.com/BobAnkh/auto-generate-changelog/blob/master/CHANGELOG.md) for changes

### Feature

- dockerfile:
  - avoid additional update ([c1346a9](https://github.com/BobAnkh/auto-generate-changelog/commit/c1346a99d527744b6464960f1ade9f384bc61a31))

### Bug Fixes

- dockerfile:
  - add update for apt ([08926c6](https://github.com/BobAnkh/auto-generate-changelog/commit/08926c6448547563aac0fb34fe5d77928d79f43a))

### Documentation

- README:
  - format table ([a7500d3](https://github.com/BobAnkh/auto-generate-changelog/commit/a7500d31865196b3c10d0fc60b5aa3b06750d956))

- CONTRIBUTING:
  - update format ([7470c9d](https://github.com/BobAnkh/auto-generate-changelog/commit/7470c9d22e4837ec81f99187fdf1d3b2c8132b02))

### Performance Improvements

- dockerfile:
  - specify git version ([6f807b5](https://github.com/BobAnkh/auto-generate-changelog/commit/6f807b5e2faef7aa040800dc005cc1b6298a9159))
  - optimize prerequists ([f45ecd1](https://github.com/BobAnkh/auto-generate-changelog/commit/f45ecd197b44c618efafc366a6946b0649756d80))

## [v0.0.2](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v0.0.2) - 2020-08-10 03:57:49

Please [CHANGELOG](https://github.com/BobAnkh/auto-generate-changelog/blob/master/CHANGELOG.md)

### Feature

- changelog:
  - add newline after list item ([f9ed121](https://github.com/BobAnkh/auto-generate-changelog/commit/f9ed121906994757e380851ef77415b48b865d13))

- codecov:
  - add coverage report ([1a3e15a](https://github.com/BobAnkh/auto-generate-changelog/commit/1a3e15a4bdf7850688f925dd0b1d8ace52e75fc3)) ([#3](https://github.com/BobAnkh/auto-generate-changelog/pull/3))

### Bug Fixes

- dockerfile:
  - use chmod to deal with  execution permission issue ([6089466](https://github.com/BobAnkh/auto-generate-changelog/commit/60894669e73d634d84aab1aee79476406ec60d45))

- main:
  - deal with DeprecationWarning ([50cfdf3](https://github.com/BobAnkh/auto-generate-changelog/commit/50cfdf32ec07b81d3140b9a06fd5275fc69f8f7b))

### Documentation

- CONTRIBUTING:
  - refactor to have styleguide ([de4c460](https://github.com/BobAnkh/auto-generate-changelog/commit/de4c46091900679835c0a005435aa447b6aea1db))

- README:
  - change `parameters` to `inputs` ([74e884d](https://github.com/BobAnkh/auto-generate-changelog/commit/74e884d18af0cab2ddbe61554d962ef55d105d6c))

- CONTRIBUTING.md:
  - fix typo and change a word ([6721474](https://github.com/BobAnkh/auto-generate-changelog/commit/6721474cb8d4b5d862389690981de72ad09b62cb))

### Performance Improvements

- main:
  - improve regex match ([0591844](https://github.com/BobAnkh/auto-generate-changelog/commit/0591844384a8a62f13eac0cec35d34df66dd07b9))

- changelog:
  - simplify progress of updating ([dd778cb](https://github.com/BobAnkh/auto-generate-changelog/commit/dd778cbc48b3e8c306e06773f499e06e46f18269))

## [v0.0.1](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v0.0.1) - 2020-07-30 02:40:43

See [CHANGELOG](https://github.com/BobAnkh/auto-generate-changelog/blob/master/CHANGELOG.md) for changes

### Feature

- main:
  - ignore docs(changelog) to appear ([93df662](https://github.com/BobAnkh/auto-generate-changelog/commit/93df662038b0e7fdf569deaab7c2dc221c127039))
  - bypass empty section ([fd47996](https://github.com/BobAnkh/auto-generate-changelog/commit/fd479964d9233f93bb6e692ba5f0692e92cf8a5a))

- CHANGELOG:
  - add main script ([5de4459](https://github.com/BobAnkh/auto-generate-changelog/commit/5de4459403ffd65976bed5051620e216092e67e4))

### Bug Fixes

- main:
  - fix a typo of regex ([fc73d2a](https://github.com/BobAnkh/auto-generate-changelog/commit/fc73d2a1167b9a7ce2689bffee4aa1250de71704))

- unrelease:
  - fix unreleased info ([ae5603d](https://github.com/BobAnkh/auto-generate-changelog/commit/ae5603d57a9f7727a75394f991bb83b3f70e943d))

- git:
  - install git ([b326c02](https://github.com/BobAnkh/auto-generate-changelog/commit/b326c02b6c2f73e62eb65261a5e60df0be90d2de))
  - install git ([97dd067](https://github.com/BobAnkh/auto-generate-changelog/commit/97dd067005e97e3359d70bd7e930c7a7637a6a72))

- permission:
  - change permission of main.py ([f8bef73](https://github.com/BobAnkh/auto-generate-changelog/commit/f8bef73840ffbc4a6975d1340c711a14838a8e88))
  - change bash script's permission ([dfb2273](https://github.com/BobAnkh/auto-generate-changelog/commit/dfb2273d070fc6e9ffda3a958fa3684f58a188ea))

### Documentation

- *:
  - update usage ([70796e5](https://github.com/BobAnkh/auto-generate-changelog/commit/70796e5b5f4d8f17e14b15eb78e0e22ab2b94864))
  - update README for usage and  add contributing guidelines ([3a69c33](https://github.com/BobAnkh/auto-generate-changelog/commit/3a69c33712178488b2fe3f1407cf26d6a5ab4ed4))

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*
