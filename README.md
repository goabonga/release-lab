# release-lab

🧪 **release-lab** is a sandbox repository used to test and validate workflows, tools, and configurations for releasing Python open-source projects.

This lab aims to serve as a base for reusable and reliable infrastructure before applying it to production repositories.

---

## 🔧 Goals

- ✅ Test CI/CD pipelines (GitHub Actions, Poetry, etc.)
- ✅ Validate PyPI publishing (with `poetry publish`)
- ✅ Experiment with changelog automation (Commitizen, Semantic Releases)
- ✅ Provide a reference `pyproject.toml` setup
- ✅ Maintain clean versioning & release management workflows
- ✅ Serve as a foundation template for future open source repositories

---

## 🛠️ Tooling

- **Poetry** – Dependency and packaging management
- **GitHub Actions** – CI/CD, test & release workflows
- **Commitizen** – Conventional commits and changelog generation
- **Pytest** – Optional testing framework
- **MkDocs** – (optional) Documentation tooling

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone git@github.com:goabonga/release-lab.git
cd release-lab
```

# Install dependencies

```bash
poetry install --with dev
```
# Run tests (if any)

```bash
poetry run pytest
```

# Prepare release (commitizen bump, poetry build, etc.)

```bash
cz bump
poetry build
```

# 📝 License

This project is licensed under the MIT License © 2025 Chris
