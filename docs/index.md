# Welcome to `release-lab` 👋

**`release-lab`** is a sandbox repository designed to test, validate, and document open-source Python project workflows — including packaging, release automation, testing, documentation, and CI/CD.

This project follows modern Python standards with tools like:
- [`poetry`](https://python-poetry.org/) for packaging and dependency management
- [`commitizen`](https://commitizen-tools.github.io/commitizen/) for versioning and changelog generation
- [`mkdocs`](https://www.mkdocs.org/) for documentation
- [`pytest`](https://docs.pytest.org/) and `mypy`, `ruff`, `isort` for quality assurance

---

## 🚀 Getting Started

### 1. Clone & install

```bash
git clone https://github.com/goabonga/release-lab.git
cd release-lab
poetry install --with dev
```

### 2. Run the CLI

```bash
poetry run hello
poetry run hello Alice
```

### 3. Run tests

```bash
make test
```

## 📘 What's Inside

 - 🧪 Testing setup with pytest, pytest-cov
 - 🔍 Type checking with mypy, linting with ruff & isort
 - 🧱 Automatic versioning with commitizen
 - 📚 Documentation with mkdocs + mkdocstrings
 - 🛠️ Fully reproducible and configurable via pyproject.toml

## 💡 Example Use Case

You can use release-lab as a starting point or a testing ground to:

 - Validate PyPI packaging and release flows
 - Prototype CI/CD and test workflows
 - Ensure docstring quality and automatic API docs
 - Build a strong foundation for new open-source Python projects
 