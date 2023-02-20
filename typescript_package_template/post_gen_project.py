"""
post_gen_project - Perform some actions that are not templated.
"""

# built-in
from pathlib import Path
import subprocess

# third-party
from vcorelib.task.subprocess.run import is_windows


def cmd(*args: str, check: bool = True) -> None:
    """Run a shell command."""
    arg_list = [*args]
    if is_windows() and not arg_list[0].endswith(".exe"):
        arg_list[0] += ".exe"
    subprocess.run(arg_list, check=check)


def git_cmd(*args: str, check: bool = True) -> None:
    """Run a 'git' command."""
    cmd("git", *args, check=check)


def mk_cmd(*args: str, check: bool = True) -> None:
    """Run an 'mk' command."""
    cmd("mk", *args, check=check)


def npm_cmd(*args: str, check: bool = True) -> None:
    """Run an 'npm' command."""
    cmd("npm", *args, check=check)


def initialize() -> None:
    """Initialize a repository, 'config' sub-module."""

    git_cmd("init")
    git_cmd("submodule", "add", "https://github.com/vkottler/config")
    git_cmd("submodule", "update", "--init", "--recursive")


def commit() -> None:
    """
    Stage everything and commit, it's okay if committing doesn't work (e.g.
    running in CI).
    """

    git_cmd("add", "-A")
    git_cmd("commit", "-m", "Initial commit.", check=False)


# Core packages.
PACKAGES = ["typescript"]

# Frameworks.
PACKAGES.append("preact")
PACKAGES.append("parcel")

# Unit testing.
PACKAGES += ["jest", "ts-jest", "@types/jest", "jest-environment-jsdom"]

# Linting.
PACKAGES += [
    "prettier",
    "eslint",
    "@typescript-eslint/eslint-plugin",
    "@typescript-eslint/parser",
    "eslint-plugin-simple-import-sort",
    "csslint",
]

# Link package name to the 'src' directory.
proj = Path("{{cookiecutter.project_name}}")
proj.symlink_to("src", target_is_directory=True)

# Set up 'config' sub-module;
initialize()

# Render everything.
mk_cmd("dz-sync")

# Install packages.
for package in PACKAGES:
    npm_cmd("install", "--save-dev", package)

# Run formatting and linting.
mk_cmd("format")
mk_cmd("lint", "yaml")
mk_cmd("test")

commit()
