# pyrig-resources

<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-resources/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-resources/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-resources/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-resources/actions/workflows/deploy.yml)
<!-- testing -->
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-resources/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-resources)
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
<!-- code-quality -->
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-resources?style=social)](https://github.com/Winipedia/pyrig-resources)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://Winipedia.github.io/pyrig-resources)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-resources?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-resources)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-resources)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-resources)](https://github.com/Winipedia/pyrig-resources/blob/main/LICENSE)

---

> A pyrig plugin that adds resources support.

---

## Overview

pyrig-resources is a [pyrig](https://github.com/Winipedia/pyrig) plugin that adds
a conventional `rig/resources/` package to your project — a home for the static
files (templates, data, assets) that ship with your package.

## What it adds

- **Resources package** — `pyrig sync` creates and maintains a `rig/resources/`
  package in your project, ready for your static files.

## Usage

```bash
uv add pyrig-resources --dev
uv run pyrig sync
```

Afterwards the package lives at `src/<your_project>/rig/resources/`.

## Documentation

Full documentation, including the auto-generated API reference, is available on
the [documentation site](https://Winipedia.github.io/pyrig-resources).
