"""Plotting utilities for the pyap movies app.

The functions in this module are plain matplotlib code with no Shiny
dependencies, so they can be called from the app, from a test, or from
the Python console.
"""

import matplotlib.pyplot as plt
import pandas as pd


def scatter_plot(df, x_var, y_var, col_var, alpha_var, size_var, title=""):
    """Create a scatter plot colored by a categorical variable.

    Draws one scatter layer per category in `col_var`, so each category
    gets its own color and legend entry. Axis labels and the legend title
    are built from the column names (underscores become spaces, and each
    word is capitalized).

    Parameters
    ----------
    df : pandas.DataFrame
        Data containing the columns named in `x_var`, `y_var`, and
        `col_var`.
    x_var : str
        Name of the numeric column mapped to the x axis.
    y_var : str
        Name of the numeric column mapped to the y axis.
    col_var : str
        Name of the categorical column used to color the points. Rows
        with a missing value in this column are not plotted.
    alpha_var : float
        Point transparency, from 0 (transparent) to 1 (opaque).
    size_var : float
        Point size. The marker area is `size_var ** 2 * 10`.
    title : str, optional
        Plot title. The default (an empty string) leaves the plot
        untitled.

    Returns
    -------
    matplotlib.figure.Figure
        The figure holding the scatter plot.

    Notes
    -----
    Colors come from the matplotlib `tab10` colormap, which repeats
    after ten categories.

    Examples
    --------
    >>> import pandas as pd
    >>> from pyap.utils import scatter_plot
    >>> movies = pd.read_csv("movies.csv")
    >>> fig = scatter_plot(movies, "critics_score", "audience_score",
    ...                    "mpaa_rating", 0.4, 3)
    """
    fig, ax = plt.subplots()

    categories = sorted(df[col_var].dropna().unique())
    cmap = plt.get_cmap("tab10")

    for i, cat in enumerate(categories):
        subset = df[df[col_var] == cat]
        ax.scatter(
            subset[x_var],
            subset[y_var],
            alpha=alpha_var,
            s=size_var ** 2 * 10,
            color=cmap(i % 10),
            label=str(cat),
        )

    ax.set_xlabel(x_var.replace("_", " ").title())
    ax.set_ylabel(y_var.replace("_", " ").title())
    if title:
        ax.set_title(title)
    ax.legend(
        title=col_var.replace("_", " ").title(),
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )
    ax.grid(alpha=0.3)
    plt.tight_layout()

    return fig
