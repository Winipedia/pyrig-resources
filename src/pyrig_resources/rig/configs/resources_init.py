"""Configuration for generating the target project's `rig/resources/__init__.py`."""

from types import ModuleType

from pyrig.rig.configs.base.init import CopyInitDocstringConfigFile

from pyrig_resources.rig import resources


class ResourcesInitConfigFile(CopyInitDocstringConfigFile):
    """Config file for the target project's `rig/resources/__init__.py`."""

    def copy_module(self) -> ModuleType:
        """Return this plugin's `resources` package."""
        return resources
