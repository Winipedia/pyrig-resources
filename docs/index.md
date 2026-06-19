# pyrig-resources Documentation

<!-- security -->
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-resources/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-resources/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-resources/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-resources/actions/workflows/deploy.yml)
<!-- code-quality -->
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
<!-- testing -->
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-resources/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-resources)
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-resources?style=social)](https://github.com/Winipedia/pyrig-resources)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- documentation -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://www.mkdocs.org)
[![Documentation](https://img.shields.io/badge/Docs-GitHub%20Pages-black?style=for-the-badge&logo=github&logoColor=white)](https://Winipedia.github.io/pyrig-resources)
<!-- project-info -->
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-resources?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-resources)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-resources)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-resources)](https://github.com/Winipedia/pyrig-resources/blob/main/LICENSE)

---

> A pyrig plugin that adds resources support.

---

## What it does

Drop-in [pyrig](https://github.com/Winipedia/pyrig) plugin that gives your
project a conventional home for static resource files:

- Adds a `rig/resources/` package to the target project, created and kept in
  place by `pyrig sync`.

No configuration required — installing the package as a development dependency
is the whole setup. Then regenerate your pyrig configs as usual and the plugin's
config file is picked up automatically.

## Installation

```bash
uv add --group dev pyrig-resources
uv run pyrig sync
```

After running `pyrig sync`, the package lives at
`src/<your_project>/rig/resources/`, ready for your static files.

## How it works

The plugin subclasses one pyrig base class:

- `InitConfigFile` (as `ResourcesInitConfigFile`) to declare the
  `rig/resources/` package. pyrig's cross-package subclass discovery finds this
  config during `sync`, resolves the source module's dotted name into your
  project's package tree, and writes the generated `__init__.py` — seeding it
  with the docstring of the plugin's own `resources` package.

---
