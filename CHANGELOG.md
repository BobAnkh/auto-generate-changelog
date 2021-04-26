# CHANGELOG

## Unreleased

Changes unreleased.

### Documentation

- README:
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
