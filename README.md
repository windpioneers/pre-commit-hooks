# pre-commit-hooks
Git hooks for use enforcing code quality, for use with [pre-commit](https://pre-commit.com/#new-hooks).

## check-branch-name

Ensures that branch names comply with at least one regex.

Every team will have different requirements. At windpioneers, we use something like:

- ``master`` for the master branch
- ``staging`` for the staging branch
- ``review/xyz`` for review branches
- ``hotfix/xyz`` for emergency fix branches directly off master
- ``learning/xyz`` for @nvn-nil's learning / experimentation
- ``devops/xyz`` for devops related improvements
- ``feature/xyz`` for new features
- ``fix/xyz for`` specific bug fixes
- ``develop/xyz`` for general experimentation or work not related to a specific feature, e.g. refactoring or testing
- ``doc/xyz`` for work improving or developing documentation

Our ``xyz`` descriptor is in kebab-case (``([a-z][a-z0-9]*)(-[a-z0-9]+)*``) as in the example below.
Other useful regexes you might need for your team are snake_case (``([a-z][a-z0-9]*)(_[a-z0-9]+)*``) and 
lowerCamelCase (``[a-z][a-zA-Z0-9]+``).
 
You can play with regexes (make sure to use the python flavour) at [
regex101.com](
https://regex101.com/)
 
Use this hook in your `.pre-commit-config.yaml` file like:
```yaml
  - repo: https://github.com/windpioneers/pre-commit-hooks
    rev: 0.0.1
    hooks:
      - id: check-branch-name
        args: 
          - '^master$'
          - '^dev$'
          - '^staging$'
          - '^develop/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
          - '^devops/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
          - '^doc/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
          - '^feature/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
          - '^fix/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
          - '^hotfix/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
          - '^learning/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
          - '^review/([a-z][a-z0-9]*)(-[a-z0-9]+)*$'
        language_version: python3
```

