"""Config that scaffolds the target project's `rig/resources/` package.

When a project installs this plugin, `pyrig sync` uses this config to create
that package, giving the project a conventional home for static resource files.
"""

from types import ModuleType

from pyrig.rig.configs.base.init import InitConfigFile

from pyrig_resources.rig import resources


class ResourcesInitConfigFile(InitConfigFile):
    """Config file that creates a project's `rig/resources/__init__.py`.

    pyrig discovers this automatically in any project that installs this
    plugin; `pyrig sync` then generates the file, seeded with the docstring
    of the resources package it copies.
    """

    def copy_module(self) -> ModuleType:
        """Return this plugin's `resources` package."""
        return resources
