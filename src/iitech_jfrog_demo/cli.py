"""CLI for iitech-jfrog-multipypi-demo."""

from __future__ import annotations

import platform
from importlib.metadata import PackageNotFoundError, version

from . import __version__ as package_version

_DISTRIBUTION = "iitech-jfrog-multipypi-demo"


def _safe_version(dist_name: str, fallback: str) -> str:
    try:
        return version(dist_name)
    except PackageNotFoundError:
        return fallback


def _module_version(module: object, dist_name: str) -> str:
    return getattr(module, "__version__", _safe_version(dist_name, "unknown"))


def main() -> None:
    """Print package, Python, and dependency versions."""
    import dateutil
    import pydantic
    import requests
    import rich

    resolved_pkg_version = _safe_version(_DISTRIBUTION, package_version)

    print(f"{_DISTRIBUTION} version: {resolved_pkg_version}")
    print(f"Python version: {platform.python_version()}")
    print(f"requests version: {_module_version(requests, 'requests')}")
    print(f"pydantic version: {_module_version(pydantic, 'pydantic')}")
    print(f"python-dateutil version: {_module_version(dateutil, 'python-dateutil')}")
    print(f"rich version: {_module_version(rich, 'rich')}")
