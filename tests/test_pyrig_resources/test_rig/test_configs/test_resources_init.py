"""Test module."""

from pyrig_resources.rig import resources
from pyrig_resources.rig.configs.resources_init import ResourcesInitConfigFile


class TestResourcesInitConfigFile:
    """Test class."""

    def test_copy_module(self) -> None:
        """Test method."""
        assert ResourcesInitConfigFile.I.copy_module() is resources
        assert resources.__doc__ == """Resource files for this project."""
