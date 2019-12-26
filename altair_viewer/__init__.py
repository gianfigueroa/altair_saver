"""Altair viewer provides offline viewing for Altair charts."""

__version__ = "0.1.0.dev0"
__all__ = ["ChartViewer", "display", "render", "show"]

from altair_viewer._core import ChartViewer

_global_viewer = ChartViewer()
display = _global_viewer.display
render = _global_viewer.render
show = _global_viewer.show
