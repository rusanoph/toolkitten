from typing import *
import matplotlib.pyplot as plt

class PlotFunction(Protocol):
    """
    A callable that draws a plot on a given matplotlib Axes object.

    This protocol defines the interface for plot functions that are used in `plot_subplots`.
    Each function must accept a `matplotlib.axes.Axes` instance and any number of keyword
    arguments, which may include plot-specific customization options.

    Example:
        ```python
        def my_plot(ax: plt.Axes, color: str = "blue") -> None:
            ax.plot([0, 1], [0, 1], color=color)

        fn: PlotFunction = my_plot
        ```

    Signature:
        (ax: plt.Axes, **kwargs) -> None
    """
    def __call__(self, ax: plt.Axes, **kwargs) -> None: ...

