# release-lab

[![codecov](https://codecov.io/github/goabonga/release-lab/branch/main/graph/badge.svg?token=CVBKEN7GA1)](https://codecov.io/github/goabonga/release-lab)

A sandbox repository used to test and validate workflows, tools, and configurations for releasing Python open-source projects.

This lab aims to serve as a base for reusable and reliable infrastructure before applying it to production repositories.

---

## Goals

- Test CI/CD pipelines (GitHub Actions, Poetry, etc.)
- Validate PyPI publishing (with `poetry publish`)
- Experiment with changelog automation (Commitizen, Semantic Releases)
- Provide a reference `pyproject.toml` setup
- Maintain clean versioning & release management workflows
- Serve as a foundation template for future open source repositories

---

## Tooling

- **Poetry** -- Dependency and packaging management
- **GitHub Actions** -- CI/CD, test & release workflows
- **release-please** -- Automated releases with monorepo support (app + Helm chart)
- **Pytest** -- Testing framework with coverage
- **MkDocs** -- Documentation generation and deployment
- **Docker** -- Container image published to GHCR
- **Helm** -- Kubernetes chart published to GHCR (OCI)

---

## CI/CD Pipelines

### Test & Lint (`tests.yml`)

Triggered on **pull requests** and **push to main**.

| Job | Description |
|-----|-------------|
| **Lint** | SPDX license headers, isort, ruff (runs once) |
| **Test** | mypy + pytest (matrix: Python 3.10 -- 3.13) |
| **Test Plan** | Updates PR body with per-check checkboxes (PR only) |

On pull requests, lint and test failures are reported as comments on the PR. Comments are automatically deleted when checks pass.

### Release (`release.yml`)

Triggered on **push to main**. Uses [release-please](https://github.com/googleapis/release-please) with monorepo support for independent versioning of the app and Helm chart.

| Job | Description |
|-----|-------------|
| **Release Please** | Creates/updates release PRs, bumps versions, generates changelogs |
| **Build** | Builds Python distribution (triggered on app release) |
| **Publish PyPI** | Publishes package to PyPI |
| **Publish Docker** | Builds and pushes Docker image to GHCR |
| **Deploy Docs** | Builds and deploys MkDocs to gh-pages |
| **Publish Helm** | Packages and pushes Helm chart to GHCR (triggered on chart release only) |

Two independent components:
- **`release-lab`** (root) -- Python app, tags: `v0.23.0`
- **`release-lab-chart`** (`chart/release-lab`) -- Helm chart, tags: `release-lab-chart-v0.1.0`

---

## Getting Started

```bash
git clone git@github.com:goabonga/release-lab.git
cd release-lab
poetry install --with dev
```

### Run tests

```bash
poetry run pytest
```

### Run linters

```bash
poetry run ruff check .
poetry run isort . --check-only --diff
poetry run mypy src/ tests/
```

### Docker

```bash
docker build -t release-lab .
docker run --rm release-lab World
```

### Helm

```bash
helm install release-lab chart/release-lab
```

### Release

Releases are automated via release-please. Simply push conventional commits to `main`:
- `feat:` triggers a minor version bump
- `fix:` triggers a patch version bump
- `feat!:` or `BREAKING CHANGE:` triggers a major version bump

release-please will create a PR with the version bump and changelog. Merge it to publish.

---

## License

This project is licensed under the MIT License.
