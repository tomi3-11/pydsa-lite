"""Tests for package metadata and importability."""

import pydsa_lite


def test_package_has_version() -> None:
    assert pydsa_lite.__version__ == "0.1.0"


def test_package_version_is_string() -> None:
    assert isinstance(pydsa_lite.__version__, str)
