"""Config that scaffolds a ``rig/resources/`` package in pyrig projects.

Defines :class:`ResourcesInitConfigFile`, a config file subclass that pyrig
discovers automatically when this plugin is installed as a dependency. Running
``pyrig mkroot`` then creates a ``rig/resources/__init__.py`` inside the target
project, giving it a conventional home for static resource files.
"""

from types import ModuleType

from pyrig.rig.configs.base.init import InitConfigFile

from pyrig_resources.rig import resources


class ResourcesInitConfigFile(InitConfigFile):
    """Generate the target project's ``rig/resources/__init__.py``.

    This config file is picked up by pyrig's cross-package subclass discovery
    when ``pyrig mkroot`` runs in any project that depends on this plugin. The
    inherited :class:`~pyrig.rig.configs.base.init.InitConfigFile` machinery
    resolves the source module's dotted name into the target project's package
    tree, so ``pyrig_resources.rig.resources`` maps to
    ``src/<project>/rig/resources/__init__.py``. The generated file carries the
    docstring of the :mod:`pyrig_resources.rig.resources` package, marking the
    directory as the project's location for static resource files.
    """

    def copy_module(self) -> ModuleType:
        """Return the module whose docstring seeds the generated package.

        Returns:
            The :mod:`pyrig_resources.rig.resources` package, whose dotted name
            determines the generated file's location (``rig/resources/``) and
            whose docstring becomes the content of the generated
            ``__init__.py``.
        """
        return resources
