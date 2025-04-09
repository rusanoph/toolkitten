class InsufficientSubplotsError(Exception):
    """
    Raised when the computed subplot grid is too small to fit all the given plots.

    This exception is raised in `plot_subplots` if the layout computed by
    `subplot_arrangement` does not provide enough subplots to display all plot functions.

    Args:
        message (str): Human-readable error message.

    Example:
        ```python
        raise InsufficientSubplotsError("Grid too small: 2x2 < 5 plots")
        ```
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)