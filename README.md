# auto-generate-changelog

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/47a06388ecd34ff5a1d623827d9bb659)](https://www.codacy.com/manual/bobankhshen/auto-generate-changelog/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BobAnkh/auto-generate-changelog&amp;utm_campaign=Badge_Grade)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/BobAnkh/auto-generate-changelog?color=orange&logo=github-actions)
![language-python](https://img.shields.io/github/languages/top/BobAnkh/auto-generate-changelog?logo=python&logoColor=yellow)
![LICENSE Apache-2.0](https://img.shields.io/github/license/BobAnkh/auto-generate-changelog?logo=apache)

A Github Action to generate CHANGELOG automatically according to conventional commits.

Feel free to submit a pull request or an issue, but make sure to follow the templates.

Welcome contributors to improve this project together!

**If you like this, please give me a star!**

## Usage

Create a workflow file such as `.github/workflows/changelog.yml` (you can find it in this repo)

```yaml
name: Generate changelog
on:
  release:
    types: [created, edited]

jobs:
  generate-changelog:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0
    - uses: BobAnkh/auto-generate-changelog@master
      with:
        REPO_NAME: '<YourUserName>/<YourRepoName>'
        ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
        PATH: '/CHANGELOG.md'
        COMMIT_MESSAGE: 'docs(CHANGELOG): update release notes'
        TYPE: 'feat:Feature,fix:Bug Fixes,docs:Documentation,refactor:Refactor,perf:Performance Improvements'
```

> NOTE: Generating CHANGELOG needs all the commit history so you should set `fetch-depth: 0` with `actions/checkout`
>
> NOTE: commit log begins with `docs(changelog)` or `doc(CHANGELOG)` will not be added to the CHANGELOG

### Inputs

**Please see notes below the table for more optional features**.

| Inputs         | Description                                                 | Required | Default                                                   |
| -------------- | ----------------------------------------------------------- | -------- | --------------------------------------------------------- |
| REPO_NAME      | Repository name                                             | no       | `''` which means current repository                       |
| ACCESS_TOKEN   | Github Access Token                                         | yes      | You can just pass `${{secrets.GITHUB_TOKEN}}`             |
| PATH           | Path to the your file                                       | no       | `/CHANGELOG.md`                                           |
| BRANCH         | The branch to update file specified in PATH                 | no       | `''` which means default branch                           |
| PULL_REQUEST   | Open a new pull request if set to a target branch name      | no       | `''` which means not open pull request by default         |
| COMMIT_MESSAGE | commit message                                              | no       | `docs(CHANGELOG): update release notes`                   |
| TYPE           | The type of commits you want to add to CHANGELOG            | no       | `'feat:Feature,fix:Fix'`                                  |
| COMMITTER      | The committer you want to use to update file                | no       | `''` which means default committer                        |

> `${{secrets.GITHUB_TOKEN}}` has a rate limit smaller than Personal Access Token, so if you have much more requests(commits, prs, etc.), use PAT instead.
>
> `COMMITTER` should be in the format: `'author <author.example>'`
> 
> NOTE: `PULL_REQUEST` must be used with `BRANCH` together, both **should be provided** if you want to **open a pull request**
> 
> You can define the keyword detected from commit message and the corresonding word presented in the changelog in input `TYPE`. For example, define `feat:Feature` will detect commit message like `feat(main): add new option` and present this in changelog as part `Feature`
>
> NOTE: You can use format below to avoid some lines in release description to appear in CHANGELOG:
>
> ```markdown
> <!-- HIDE IN CHANGELOG BEGIN -->
> See CHANGELOG for more details.
> <!-- HIDE IN CHANGELOG END -->
> ```

## Maintainer

[@BobAnkh](https://github.com/BobAnkh)

## How to contribute

You should follow our [Code of Conduct](/CODE_OF_CONDUCT.md).

See [CONTRIBUTING GUIDELINES](/CONTRIBUTING.md) for contributing conventions.

Make sure to pass all the tests before submitting your code. You can conduct `pytest -ra` at the root directory to run all tests.

You can use local mode when develope it on your local machine, here is the command-line help info:

```console
usage: main.py [-h] [-m MODE] [-f FILE] [-o OUTPUT] [-t TOKEN]

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  choose to use local-dev mode or on github action mode.
                        Valid values are 'local' or 'github'
  -f FILE, --file FILE  configuration file to read from when running local-dev
                        mode
  -o OUTPUT, --output OUTPUT
                        output file when running local-dev mode
  -t TOKEN, --token TOKEN
                        Github Access Token
```

### Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/BobAnkh>
            <img src=https://avatars.githubusercontent.com/u/44333669?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=BobAnkh/>
            <br />
            <sub style="font-size:14px"><b>BobAnkh</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/sruehl>
            <img src=https://avatars.githubusercontent.com/u/1769155?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Sebastian Rühl/>
            <br />
            <sub style="font-size:14px"><b>Sebastian Rühl</b></sub>
        </a>
    </td>
</tr>
</table>

## LICENSE

[Apache-2.0](/LICENSE) © BobAnkh
