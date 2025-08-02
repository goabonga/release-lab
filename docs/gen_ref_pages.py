# docs/gen_ref_pages.py

from pathlib import Path
import mkdocs_gen_files

FILES = {
    "CODE_OF_CONDUCT.md": "code_of_conduct.md",
    "CONTRIBUTING.md": "contributing.md",
    "CHANGELOG.md": "changelog.md",
    "LICENSE": "license.md",  # important: convert to .md
}

for src_name, dest_name in FILES.items():
    src = Path(".") / src_name
    dest = Path(dest_name)

    try:
        content = src.read_text()

        # Add header for LICENSE
        if src_name == "LICENSE":
            content = f"# License\n\n```\n{content}\n```"

        with mkdocs_gen_files.open(dest, "w") as f:
            f.write(content)

    except FileNotFoundError:
        print(f"File {src} not found, skipping.")
    except Exception as e:
        print(f"An error occurred while processing {src}: {e}")
