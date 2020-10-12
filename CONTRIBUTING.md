# CONTRIBUTING

We'd be glad for you to contribute to our source code and to make this project better!

Feel free to submit a pull request or an issue, but make sure to use the templates

We adopt a series of automation tools to check, contributions not following the conventions may be rejected

Here are the contributing conventions we'd like you to follow:

## Style Guide

### Commit Message Convention

Each commit should contain relatively independent change (that is, a hodgepodge of multiple types of modifications is not allowed to be submitted in one commit), and the specific changes need to be clarified in the message

The commit message conventions of this project mainly refers to the most widely used [AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.uyo6cb12dt6w)

Here is the message format:

> `<type>(<scope>): <subject>`
>
> // blank line
>
> `<body>`
>
> // blank line
>
> `<footer>`

The `<header>` section(the first line) is mandatory for any project. The `<body>` section and `<footer>` section are optional according to the actual situation

A blank line is required between sections

Also, the `<header>` section(only contains one line) cannot be longer than 50 characters and any line of the `<body>` section cannot be longer than 72 characters

This allows the commit message to be easier to read on GitHub as well as in various git tools.

#### About `<header>` Section

The `<header>` section only contains one line and three fields(`<type>`, `<scope>` and `<subject>`) need to meet the requirements:

The `type` field mainly explains the type of the commit. Only the following 9 types are allowed to be used in `AngularJS Git Commit Message Conventions`:

- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- refactor: A code change that neither fixes a bug nor adds a feature
- perf: A code change that improves performance
- test: Adding missing or correcting existing tests
- chore: Changes to the build process or auxiliary tools and libraries such as documentation generation
- revert: If the commit reverts a previous commit, it should be followed by the `<header>`of the reverted commit and in the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted

For this project, the following 2 types can also be used if necessary:

- build: Changes to the build tools or dependencies (webpack, npm, etc)
- ci: Changes to Continuous Integration

If a commit is related to multiple `<type>`, use `feat` and `fix` in priority, followed by the remaining seven types specified in `AngularJS Git Commit Message Conventions`, and the remaining two are for special needs

The `<scope>` section mainly describes the influence scope of this commit, usually file, path or functionality. For example, name of modified file can be filled in this section (Module name of project name can be used if multiple files are modified), and feature influenced can be filled in this section. If it is a global influence, character `*` can be used

The `<subject>` section mainly summarizes the purpose and changes of this commit. It should begin with verb and use the imperative, present tense. The first letter should be lowercase and have no dot(.) at the end

#### About `<body>` Section

The `<body>` section is the text section, which contains the detailed description of this commit. It should use the imperative, present tense

This section can be bypassed if the `<header>` section is enough to summarize the entire change of this commit

It is recommended to use the dashes(-) to create an unordered list, and it should explain what problem this commit solves, how to solve it, and whether other changes have been introduced (such as necessary document updates, etc.)

#### About `<footer>` Section

The `<footer>` section is bypassed except 2 situations:

One is breaking change, that is, the current version is not compatible with the previous version. It should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the breaking change block is then the description of the change, justification and migration notes.

The other is to reference GitHub issues that this commit closes. Use format `Closes #123, #456` to close one or more issues

#### Commit Message Examples

Here are some examples of commit message:

> For example, if a new feature is to add a option for round contributor's avatar, the commit message can be written as:

```text
feat(contributor): add a option for round avatar

- add a option to choose the avatar in circle or in square
- add new template in the python script to handle it
- update usage and example in README.md

Closes #123
```

> If a new documentation of linux command ls is added, the commit message can be written as:

```text
docs(command): add linux command ls

- add basic usage format of command ls
- add arguments of command ls
- add considerations of command ls
- plan to add more typical examples in future
- plan to add descriptions in the future
```

> If it fixes a typo found in the documentation ls.md, the commit message can be written as:

```text
docs(ls.md): fix a typo

- change `-` to `--`

Closes #456
```

### Pull Request Convention

> **NOTE**: Use `rebase` method or `pull --rebase` method to update your branch so as to make the commit history clean.

The project has configured several automation check tools. Please wait a moment after your Pull Request submitted and deal with some issues according to the comments and details of check tools.

#### Branch Name

You are recommended to submit a Pull Request (PR) from a new branch with a name related to the changes. **Pull Request from master branch may cause trouble to your future work**. This is because when you open a Pull Request from a branch, you can still update the Pull Request by committing and pushing to the branch. And your master branch can be used to track the latest changes.

As for this project, the branch name of the Pull Request should follow the conventions below:

- If it is for a new feature, the branch name should begin with `feature/`, followed by the specific feature name, e.g. `feature/md2pdf` for developing a new feature `md2pdf` and `feature/optimize_md2pdf` for optimizing the feature `md2pdf`
- If it is a bug fix to a feature, the branch name should begin with `fix/`, followed by the fixed feature name, e.g. `fix/yapf` for fixing bug of feature `yapf`
- If it is only a change to documentation, the branch name should begin with `docs/`, followed by the scope of documentation change, e.g. `docs/usage` for changing the documentation of usage
- In other cases, please submit an issue to discuss with the maintainer first

#### Title of Pull Request

The title of the Pull Request should summarize the changes. It should begin with type that represents the changes. Here are some examples:

For a new feature, the title should begin with **`feature(<Your-New-Feature>):`**

For a bug fix, the title should begin with **`fix(<Your-Bugfix-Feature>)`**

For documentation changes, the title should begin with **`docs(<Your-Documentation-change-scope>)`**

#### Description of Pull Request

Please follow [pull_request_template](.github/PULL_REQUEST_TEMPLATE.md) to describe the changes of the Pull Request so that the reviewers can understand your changes more clearly. This part cannot be empty.

Motivation of this Pull Request(e.g. what problem is solved and what feature is optimized) should be clarified in the description. What feature has been implemented in this Pull Request should be described in details and the technology stack of this feature should also be introduced. Other necessary changes (e.g. relevant documentation update) also need to be declared in the description.

It is recommended to use `Tasklist` format to describe the steps or technology stack of the changes. Any `draft pull request` is recommended to contain a `Tasklist` in the description and update it when the development progresses.

> Following is the Tasklist format:
>
> [x] This is what you have done and how you achieve this.
>
> [ ] This is what you plan to do and how you plan to achieve it.

If this Pull Request fixes a issue, you should use the right format to link it in the description. You can use format like `Resolves: #123` or `Closes: #123` to close that issue when this Pull Request is merged and use format like `Ref: #123` just for reference.

Besides, please make sure that your Pull Request is not a duplicate to any assigned issue or existing Pull Request. **Screenshots** are needed for changes to html files or css files

### Language Style

Files of different languages should be checked locally according to the following conventions

Commits should be made after all checks pass

#### Markdown

Use `markdownlint` to check, configuration can see [.markdownlint.json](/.markdownlint.json)

#### Python

Use `flake8` default configuration to check and use `yapf` default configuration to format

Adopt Google's style for comments. Recommended to use vscode extension `Python Docstring Generator` to assist with

We use `Pytest` for test. Just execute command `pytest -vv` under root directory to run all the test. Please add new tests if you add new features and make sure to pass all the tests locally

#### Shell

Use `shellcheck` default configuration to check
