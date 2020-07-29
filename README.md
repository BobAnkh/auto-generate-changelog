# auto-generate-changelog

![language-python](https://img.shields.io/github/languages/top/BobAnkh/auto-generate-changelog?logo=python&logoColor=yellow)
![LICENSE Apache-2.0](https://img.shields.io/github/license/BobAnkh/auto-generate-changelog?logo=apache)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/BobAnkh/auto-generate-changelog?color=orange&logo=github-actions)

A Github Action to generate CHANGELOG automatically according to conventional commits

Feel free to submit a pull request or an issue, but make sure to follow the templates

Welcome contributors to improve this project together!

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
    - uses: BobAnkh/auto-generate-changelog@master
      with:
        REPO_NAME: 'BobAnkh/auto-generate-changelog'
        ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
        PATH: '/CHANGELOG.md'
        COMMIT_MESSAGE: 'docs(CHANGELOG): update CHANGELOG'
        FEAT: '1'
        FIX: '1'
        DOCS: '1'
        CHORE: '1'
        REFACTOR: '1'
        PERF: '1'
```

### Parameters

| Parameter | Description | Required | Default |
| --- | --- | --- | --- |
| REPO_NAME| Repository name | yes | - |
| ACCESS_TOKEN | Github Access Token | yes | You can just pass `${{secrets.GITHUB_TOKEN}}` |
| PATH | Path to the file you want to add contributors' list | no | `/CHANGELOG.md` |
| COMMIT_MESSAGE | commit message | no | `docs(CHANGELOG): update CHANGELOG` |
| FEAT | Set 1 to generate it | no | `1` |
| FIX | Set 1 to generate it | no | `1` |
| DOCS | Set 1 to generate it | no | `1` |
| CHORE | Set 1 to generate it | no | `1` |
| REFACTOR | Set 1 to generate it | no | `1` |
| PERF | Set 1 to generate it | no | `1` |

## Maintainer

[@BobAnkh](https://github.com/BobAnkh)

## How to contribute

You should follow our [Code of Conduct](/CODE_OF_CONDUCT.md)

See [CONTRIBUTING GUIDELINES](/CONTRIBUTING.md) for contributing conventions

### Contributors

<table>
<tr>
    <td align="center">
        <a href=https://github.com/BobAnkh>
            <img src=https://avatars2.githubusercontent.com/u/44333669?v=4 width="100;" style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;" alt=BobAnkh/>
            <br />
            <sub style="font-size:14px"><b>BobAnkh</b></sub>
        </a>
    </td>
</tr>
</table>

## LICENSE

[Apache-2.0](/LICENSE) © BobAnkh
