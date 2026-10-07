"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.copy_module import CopyModuleConfigFile

from pyrig_resources.rig.configs.resources_init import ResourcesInitConfigFile

_CONFIG_FILE_OVERRIDES = (CopyModuleConfigFile.copy_module,)
_CONFIG_FILES = (ResourcesInitConfigFile,)
