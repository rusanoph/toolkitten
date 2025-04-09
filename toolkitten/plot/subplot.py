from typing import *
import math

import numpy as np
from matplotlib import pyplot as plt
from .exceptions import InsufficientSubplotsError
from .types import  PlotFunction


def subplot_arrangement(
        n: int,
        ratio: Tuple[int, int] = (1, 1)
) -> Tuple[int, int]:
    """
    Compute the number of rows and columns for arranging `n` subplots with a given aspect ratio.

    The function returns a tuple `(rows, cols)` such that the grid layout approximates
    the specified ratio and fits all `n` plots.

    Given a target aspect ratio \( r = \\frac{a}{b} \), the layout is computed by:

    $$
    \\text{cols} = \\lceil r \\cdot \\sqrt{n} \\rceil, \\quad
    \\text{rows} = \\lceil \\frac{n}{\\text{cols}} \\rceil
    $$

    If \( a < b \), the result is returned as `(cols, rows)`, otherwise as `(rows, cols)`
    to better preserve the aspect.

    Args:
        n (int): Number of subplots.
        ratio (Tuple[int, int], optional): Target aspect ratio \((a, b)\). Defaults to (1, 1).

    Returns:
        Tuple[int, int]: Number of `(rows, cols)` to fit all subplots.

    Raises:
        ValueError: If `a` or `b` is zero.

    Example:
        ```python
        subplot_arrangement(9, ratio=(4, 3))  # → (3, 3)
        ```
    """
    a, b = ratio

    if a == 0 or b == 0:
        raise ValueError("Invalid ratio: both elements must be > 0")

    aspect_ratio  = min(a, b) / max(a, b)
    cols = math.ceil(aspect_ratio  * math.sqrt(n))
    rows = math.ceil(n / cols)

    return (cols, rows) if a < b else (rows, cols)


def plot_subplots(
        data: List[PlotFunction],
        title: Optional[str] = None,
        plot_params: Optional[List[Dict]] = None,
        arrangement_ratio: Tuple[int, int] = None,
        figsize_per_plot: Tuple[int, int] = (5, 4)
) -> None:
    """
        Plot multiple subplots in a grid with automatic arrangement based on the number of plots.

        This function displays a list of plotting functions in a subplot grid layout. The layout is
        computed using the `subplot_arrangement` function, optionally respecting a target aspect
        ratio \\( (a, b) \\), and each plotting function is called with its corresponding parameters.

        Args:
            data (List[PlotFunction]):
                A list of functions that take a `matplotlib.axes.Axes` object and plot on it.
            title (Optional[str], optional):
                Optional global title for the entire figure.
            plot_params (Optional[List[Dict]], optional):
                A list of dictionaries with keyword arguments to pass to each plot function.
                Defaults to empty dicts for each function.
            arrangement_ratio (Tuple[int, int], optional):
                Target aspect ratio \\( (a, b) \\) for subplot layout. If not provided, defaults to \\( (1, 1) \\).
            figsize_per_plot (Tuple[int, int], optional):
                Base size for each subplot (width, height) in inches. Defaults to (5, 4).

        Raises:
            InsufficientSubplotsError:
                If the computed grid is too small to fit all plots.

        Example:
            ```python
            plot_subplots(
                data=[plot_image(img1, "Image 1"), plot_image(img2, "Image 2")],
                title="Comparison",
                arrangement_ratio=(4, 3),
                figsize_per_plot=(6, 5)
            )
            ```
    """

    n = len(data)  # Number of plots
    cols, rows = subplot_arrangement(n, arrangement_ratio)

    # Check for p, q enough to fit all data plots
    if cols * rows < n:
        raise InsufficientSubplotsError(
            f"Not enough subplots: {cols} x {rows} < {n} plots."
        )

    if plot_params is None:
        plot_params = [{}] * n

    figsize_col, figsize_row = figsize_per_plot
    fig, axes = plt.subplots(rows, cols, figsize=(cols * figsize_col, rows * figsize_row))
    axes = np.atleast_1d(axes).flatten()

    # Plot on fig
    for ax, func, params in zip(axes[:n], data, plot_params):
        func(ax, **params)

    # Remove redundant subplots
    for ax in axes[n:]:
        fig.delaxes(ax)

    if title is not None:
        fig.suptitle(title, fontsize=24)

    plt.tight_layout()
    plt.show()