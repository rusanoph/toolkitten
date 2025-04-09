from typing import cast

import numpy as np
import matplotlib.pyplot as plt

from ..types import PlotFunction

def plot_image(img: np.ndarray, title: str, cmap: str = 'gray_r', **imshow_kwargs) -> PlotFunction:
    """
    Create a plotting function that displays a single image with a title.

    The function returns a callable `PlotFunction` that takes a Matplotlib `Axes` object and
    plots the provided image using `imshow`. A custom colormap and additional
    `imshow` parameters can be supplied.

    The image is rendered as:

    $$
    \\text{ax.imshow}(\\text{img}, \\text{cmap}, \\text{**kwargs})
    $$

    followed by setting the title via:

    $$
    \\text{ax.set_title}(\\text{title})
    $$

    Args:
        img (np.ndarray): The image to be displayed.
        title (str): Title to be shown above the image.
        cmap (str, optional): Matplotlib colormap name. Defaults to `'gray_r'`.
        **imshow_kwargs: Additional keyword arguments passed to `imshow`.

    Returns:
        PlotFunction: A function that can be passed an `Axes` to render the image.

    Example:
        ```python
        fig, ax = plt.subplots()
        plot_fn = plot_image(image_array, title="Example")
        plot_fn(ax)
        ```
    """
    def plot_function(ax: plt.Axes, **kwargs) -> None:
        ax.imshow(img, cmap=cmap, **imshow_kwargs)
        ax.set_title(title)

    return cast(PlotFunction, plot_function)
