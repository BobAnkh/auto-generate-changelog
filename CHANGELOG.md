# CHANGELOG

## Unreleased

Changes unreleased

### Features

### Bug Fixes

- main:
  - add a blank newline at the end ([9ae5e55](https://github.com/BobAnkh/auto-generate-changelog/commit/9ae5e5526238ccc48337db1bc0b0f2958e588ab5))

### Documentation Changes

### Chores

- deps:
  - bump cryptography from 3.0 to 3.1 ([445c533](https://github.com/BobAnkh/auto-generate-changelog/commit/445c5331223e7ac849b793368458a3c24be766b5)) ([#12](https://github.com/BobAnkh/auto-generate-changelog/pull/12))
  - bump pygithub from 1.52 to 1.53 ([ed57d15](https://github.com/BobAnkh/auto-generate-changelog/commit/ed57d1576c9ef83885663a30e787897c5163b985)) ([#8](https://github.com/BobAnkh/auto-generate-changelog/pull/8))
  - bump cffi from 1.14.1 to 1.14.2 ([8ac2939](https://github.com/BobAnkh/auto-generate-changelog/commit/8ac29395bdc52b82b6e91d7bed16303078844eb8)) ([#7](https://github.com/BobAnkh/auto-generate-changelog/pull/7))

- gitmagic:
  - ignore `.` in branch name check ([716fb91](https://github.com/BobAnkh/auto-generate-changelog/commit/716fb91cede8d8be466e8fa3b71f3b9169688d84))

### Refactors

### Performance Improvements

## [v0.0.3](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v0.0.3) - 2020-08-10 08:02:40

See [CHANGELOG](https://github.com/BobAnkh/auto-generate-changelog/blob/master/CHANGELOG.md) for changes

### Features

- dockerfile:
  - avoid additional update ([c1346a9](https://github.com/BobAnkh/auto-generate-changelog/commit/c1346a99d527744b6464960f1ade9f384bc61a31))

### Bug Fixes

- dockerfile:
  - add update for apt ([08926c6](https://github.com/BobAnkh/auto-generate-changelog/commit/08926c6448547563aac0fb34fe5d77928d79f43a))

### Documentation Changes

- README:
  - format table ([a7500d3](https://github.com/BobAnkh/auto-generate-changelog/commit/a7500d31865196b3c10d0fc60b5aa3b06750d956))

- CONTRIBUTING:
  - update format ([7470c9d](https://github.com/BobAnkh/auto-generate-changelog/commit/7470c9d22e4837ec81f99187fdf1d3b2c8132b02))

### Chores

### Refactors

### Performance Improvements

- dockerfile:
  - specify git version ([6f807b5](https://github.com/BobAnkh/auto-generate-changelog/commit/6f807b5e2faef7aa040800dc005cc1b6298a9159))
  - optimize prerequists ([f45ecd1](https://github.com/BobAnkh/auto-generate-changelog/commit/f45ecd197b44c618efafc366a6946b0649756d80))

## [v0.0.2](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v0.0.2) - 2020-08-10 03:57:49

Please [CHANGELOG](https://github.com/BobAnkh/auto-generate-changelog/blob/master/CHANGELOG.md)

### Features

- codecov:
  - add coverage report ([1a3e15a](https://github.com/BobAnkh/auto-generate-changelog/commit/1a3e15a4bdf7850688f925dd0b1d8ace52e75fc3)) ([#3](https://github.com/BobAnkh/auto-generate-changelog/pull/3))

- changelog:
  - add newline after list item ([f9ed121](https://github.com/BobAnkh/auto-generate-changelog/commit/f9ed121906994757e380851ef77415b48b865d13))

### Bug Fixes

- main:
  - deal with DeprecationWarning ([50cfdf3](https://github.com/BobAnkh/auto-generate-changelog/commit/50cfdf32ec07b81d3140b9a06fd5275fc69f8f7b))

- dockerfile:
  - use chmod to deal with ... ([6089466](https://github.com/BobAnkh/auto-generate-changelog/commit/60894669e73d634d84aab1aee79476406ec60d45))

### Documentation Changes

- CONTRIBUTING.md:
  - fix typo and change a word ([6721474](https://github.com/BobAnkh/auto-generate-changelog/commit/6721474cb8d4b5d862389690981de72ad09b62cb))

- README:
  - change `parameters` to `inputs` ([74e884d](https://github.com/BobAnkh/auto-generate-changelog/commit/74e884d18af0cab2ddbe61554d962ef55d105d6c))

- CONTRIBUTING:
  - refactor to have styleguide ([de4c460](https://github.com/BobAnkh/auto-generate-changelog/commit/de4c46091900679835c0a005435aa447b6aea1db))

### Chores

- *:
  - fix some typos ([e217912](https://github.com/BobAnkh/auto-generate-changelog/commit/e217912f5738c8a9e7c0a7fbd2c37e546d07a4ce))

- deps:
  - bump pygithub from 1.51 to 1.52 ([33e6b99](https://github.com/BobAnkh/auto-generate-changelog/commit/33e6b99411852635a61175950d6a6d59545c9f3c)) ([#2](https://github.com/BobAnkh/auto-generate-changelog/pull/2))

- pytest:
  - change name ([21ff26b](https://github.com/BobAnkh/auto-generate-changelog/commit/21ff26b0075845f116dfdd9c87d5a3c89fda8660))
  - change to self-written one ([dd85763](https://github.com/BobAnkh/auto-generate-changelog/commit/dd857636e1362f78aa436f8fb75886ce2f5ba54b))
  - install requirements ([4cf8e46](https://github.com/BobAnkh/auto-generate-changelog/commit/4cf8e46a803f8f6180691b0fd7ccf68343e7e161))
  - add pytest to python convention ([97aec2b](https://github.com/BobAnkh/auto-generate-changelog/commit/97aec2b5464db1b442b85e050f94b29f0261e7fe))

- gitigore:
  - ignore python-related files ([94e29d3](https://github.com/BobAnkh/auto-generate-changelog/commit/94e29d3fd772cc3787143196ed0f7b62490846b3))

- template:
  - update template style ([ec67d8b](https://github.com/BobAnkh/auto-generate-changelog/commit/ec67d8bef6350d79fed18423eb85364c7a5ff1ec))

- gitmagic:
  - update rules ([82d2f10](https://github.com/BobAnkh/auto-generate-changelog/commit/82d2f10cf6035218e2f0898be3e09fdb41b2d144))

- mdl:
  - ignore md024 and code_of_conduct ([e19c0ff](https://github.com/BobAnkh/auto-generate-changelog/commit/e19c0ffcdfb553b8bb0286f8a9ee5969661638a1))

- mergify:
  - fix a typo ([997b3c8](https://github.com/BobAnkh/auto-generate-changelog/commit/997b3c8d4f5e5253bba0d0eecbab4b6fb6e92768))

### Refactors

### Performance Improvements

- main:
  - improve regex match ([0591844](https://github.com/BobAnkh/auto-generate-changelog/commit/0591844384a8a62f13eac0cec35d34df66dd07b9))

- changelog:
  - simplify progress of updating ([dd778cb](https://github.com/BobAnkh/auto-generate-changelog/commit/dd778cbc48b3e8c306e06773f499e06e46f18269))

## [v0.0.1](https://github.com/BobAnkh/auto-generate-changelog/releases/tag/v0.0.1) - 2020-07-30 02:40:43

See [CHANGELOG](https://github.com/BobAnkh/auto-generate-changelog/blob/master/CHANGELOG.md) for changes

### Features

- main:
  - ignore docs(changelog) to appear ([93df662](https://github.com/BobAnkh/auto-generate-changelog/commit/93df662038b0e7fdf569deaab7c2dc221c127039))
  - bypass empty section ([fd47996](https://github.com/BobAnkh/auto-generate-changelog/commit/fd479964d9233f93bb6e692ba5f0692e92cf8a5a))

- CHANGELOG:
  - add main script ([5de4459](https://github.com/BobAnkh/auto-generate-changelog/commit/5de4459403ffd65976bed5051620e216092e67e4))

### Bug Fixes

- main:
  - fix a typo of regex ([fc73d2a](https://github.com/BobAnkh/auto-generate-changelog/commit/fc73d2a1167b9a7ce2689bffee4aa1250de71704))

- permission:
  - change permission of main.py ([f8bef73](https://github.com/BobAnkh/auto-generate-changelog/commit/f8bef73840ffbc4a6975d1340c711a14838a8e88))
  - change bash script's permission ([dfb2273](https://github.com/BobAnkh/auto-generate-changelog/commit/dfb2273d070fc6e9ffda3a958fa3684f58a188ea))

- git:
  - install git ([b326c02](https://github.com/BobAnkh/auto-generate-changelog/commit/b326c02b6c2f73e62eb65261a5e60df0be90d2de))
  - install git ([97dd067](https://github.com/BobAnkh/auto-generate-changelog/commit/97dd067005e97e3359d70bd7e930c7a7637a6a72))

- unrelease:
  - fix unreleased info ([ae5603d](https://github.com/BobAnkh/auto-generate-changelog/commit/ae5603d57a9f7727a75394f991bb83b3f70e943d))

### Documentation Changes

- *:
  - update usage ([70796e5](https://github.com/BobAnkh/auto-generate-changelog/commit/70796e5b5f4d8f17e14b15eb78e0e22ab2b94864))
  - update README for usage and ... ([3a69c33](https://github.com/BobAnkh/auto-generate-changelog/commit/3a69c33712178488b2fe3f1407cf26d6a5ab4ed4))

### Chores

- *:
  - add basic ci tools ([e7301db](https://github.com/BobAnkh/auto-generate-changelog/commit/e7301db4ac79b7b193c7c8be39c30b1377e25c80))

- changelog:
  - change trigger-event to release ([7cb0ddd](https://github.com/BobAnkh/auto-generate-changelog/commit/7cb0ddd983b22bd87ba319636910cd9a5a4662f0))

- CHANGELOG:
  - update config ([627e8f4](https://github.com/BobAnkh/auto-generate-changelog/commit/627e8f4e5ca648803e2045bb8b7bef70bb786ed2))

### Refactors

### Performance Improvements

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*
