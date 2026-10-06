import matplotlib.pyplot as plt
import pandas as pd


def scatter_plot(df, x_var, y_var, col_var, alpha_var, size_var, title=""):
    """Create a scatter plot of df colored by a categorical variable."""
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
    plt.tight_layout()

    return fig
