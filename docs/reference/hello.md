# `hello` module

This module provides a simple CLI command to demonstrate the release process, packaging, and distribution for a Python project using Poetry.

It is used primarily as a sandbox to validate CI/CD workflows, versioning with Commitizen, and documentation generation with MkDocs.


## Module Reference

::: hello
    options:
      show_source: true
      members_order: source
      docstring_style: google
      docstring_section_style: list
      # filters: ["!^_"]


## CLI Entry Point

The main command-line entry point exposed by the project.

```bash
poetry run hello
poetry run hello Alice
```

::: hello.cli.main
    options:
        show_source: false
        show_signature: true

