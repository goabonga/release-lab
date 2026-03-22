## v0.23.0 (2026-03-22)

### Feat

- delete PR comments when checks pass instead of updating
- list checks under all-passed summary comment
- group test plan checkboxes by Python version
- add test plan with per-check checkboxes in PR body
- update PR lint comments when checks are resolved
- add pr check errors summary

### Fix

- fix header ...
- replace peter-evans action with gh api for comment upsert
- add --repo flag to gh commands in test-plan job

### Refactor

- split lint and test into separate jobs

## [0.24.0](https://github.com/goabonga/release-lab/compare/v0.23.0...v0.24.0) (2026-03-22)


### Features

* add Dockerfile, Helm chart, Docker/Helm publish jobs, and update README ([18beba6](https://github.com/goabonga/release-lab/commit/18beba63bb9170ecd79575f2ff88892087014934))
* bump chart version only when chart files change ([2bfa869](https://github.com/goabonga/release-lab/commit/2bfa869ecf9e0908baa16d462e0afd3f1e10591c))
* decouple chart version from app version ([6810805](https://github.com/goabonga/release-lab/commit/6810805b5089e4dd2fd5a755ee1fb192610122c7))
* migrate from commitizen to release-please ([22ef9fb](https://github.com/goabonga/release-lab/commit/22ef9fbec274420f9e73a68f3d725cc5953a50aa))


### Bug Fixes

* use GITHUB_TOKEN for release-please action ([13f74b3](https://github.com/goabonga/release-lab/commit/13f74b3e90d36fbf4e132b8d43f79b404a43a686))

## v0.22.1 (2025-08-07)

### Fix

- use global env var into release pipeline

## v0.22.0 (2025-08-07)

### Feat

- cleaning up the release workflow

## v0.21.3 (2025-08-06)

### Fix

- check release signed doc

## v0.21.2 (2025-08-06)

### Fix

- check release signed doc

## v0.21.1 (2025-08-06)

### Fix

- check release signed doc

## v0.21.0 (2025-08-06)

### Feat

- check release signed doc

## v0.20.0 (2025-08-06)

### Feat

- check release signed doc

## v0.19.3 (2025-08-06)

### Fix

- remote for dependabot

## v0.19.2 (2025-08-06)

### Fix

- gh token

## v0.19.1 (2025-08-06)

### Fix

- dependabot

## v0.19.0 (2025-08-06)

### Feat

- sign rewrite and sign dependabot commits

## v0.18.6 (2025-08-06)

### Fix

- use poetry version 2.1.1

## v0.18.5 (2025-08-06)

### Fix

- use "needs.bump_and_build.outputs.version"

## v0.18.4 (2025-08-06)

### Fix

- remove codecov_tag job

## v0.18.3 (2025-08-06)

### Fix

- use name and flags

## v0.18.2 (2025-08-06)

### Fix

- use override branch for tag into codecov

## v0.18.1 (2025-08-06)

### Fix

- checkout repo for codecov

## v0.18.0 (2025-08-06)

### Feat

- test to publish a new release

## v0.17.0 (2025-08-06)

### Feat

- test to publish a new release

## v0.16.0 (2025-08-06)

## v0.16.0 (2025-08-06)

### Feat

- upload coverage and tests result for tag
- test to publish a new release

### Fix

- use bump_version into build_and_tag step

## v0.15.0 (2025-08-06)

### Feat

- use matrix in tests

### Fix

- set project name into pipeline
- get tags on tests step into release pipeline

## v0.14.0 (2025-08-05)

### Feat

- exec tests pipeline on any pr

### Fix

- set id to run tests for conditional checking
- set conditional upload to codecover

## v0.13.0 (2025-08-05)

### Feat

- add isort check on tests pipeline

### Fix

- apply isort

## v0.12.0 (2025-08-05)

### Feat

- release clean version

## v0.11.0 (2025-08-05)

### Feat

- fix documentation plugins

## v0.10.12 (2025-08-05)

### Fix

- fix mkdocs current version

## v0.10.11 (2025-08-05)

### Fix

- pipeline
- bump temporary version in tests

## v0.10.10 (2025-08-05)

### Fix

- doc version

## v0.10.9 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.8 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.7 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.6 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.5 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.4 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.3 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.2 (2025-08-05)

### Fix

- version format in pipeline

## v0.10.1 (2025-08-05)

### Fix

- fix pipeline

## v0.10.0 (2025-08-05)

### Feat

- split jobs

## v0.9.0 (2025-08-05)

### Feat

- use personal token

## v0.8.0 (2025-08-05)

### Feat

- release

## v0.7.0 (2025-08-05)

### Feat

- Publish to TestPyPI

## v0.6.1 (2025-08-05)

### Fix

- upload tests report to codecov

## v0.6.0 (2025-08-05)

### Feat

- upload test result
- publish coverage to Codecov

### Fix

- commitizen use version into pyproject

## v0.5.1 (2025-08-05)

### Fix

- fix test version file name

## v0.5.0 (2025-08-05)

### Feat

- check licenses

### Fix

- use __expected_version__ in test_version

## v0.4.0 (2025-08-05)

### Feat

- signed tags with gpg key

## v0.3.0 (2025-08-02)

### Feat

- release doc

## v0.2.0 (2025-08-02)

### Feat

- publish a new release
- trigger release

## v0.1.0 (2025-08-02)

### Feat

- **init**: initialize project structure, tooling, and CI
