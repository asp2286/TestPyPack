"""iitech_jfrog_demo package."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

_DISTRIBUTION = "iitech-jfrog-multipypi-demo"

try:
    __version__ = version(_DISTRIBUTION)
except PackageNotFoundError:  # pragma: no cover - fallback for editable/uninstalled
    __version__ = "0.0.0"

__all__ = ["__version__"]
