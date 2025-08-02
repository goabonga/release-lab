## ✅ `docs/cli.md`

# CLI usage

The `release-lab` project provides a simple command-line interface using [`click`](https://click.palletsprojects.com/).

You can call it using Poetry:

```bash
poetry run hello
poetry run hello <your-name>
```

### 🧪 Examples
Greet the world

```bash
poetry run hello
```

Output:

```bash
Hello, world!
```

Greet someone by name

```bash
poetry run hello Alice
```

Output:

```bash
Hello, Alice!
```

### 📦 How it works

The CLI is defined in src/hello/cli.py using the @click.command() decorator and is registered in pyproject.toml under:

```toml
[tool.poetry.scripts]
hello = "hello.cli:main"
```

This makes it available as a hello command when installed via Poetry or published on PyPI.