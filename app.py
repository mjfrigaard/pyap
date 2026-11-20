# This is a Shiny for Python application.
# Run it with: shiny run app.py

from shiny import App, ui, render
import matplotlib.pyplot as plt
import numpy as np

# Old Faithful geyser waiting time data (bimodal distribution)
rng = np.random.default_rng(42)
waiting = np.concatenate([
    rng.normal(54, 5, 100),   # short-wait eruption cluster
    rng.normal(80, 6, 172),   # long-wait eruption cluster
])

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider(
            "bins",
            "Number of bins:",
            min=1,
            max=50,
            value=30,
        ),
    ),
    ui.output_plot("distPlot"),
    title="Old Faithful Geyser Data",
)


def server(input, output, session):
    @render.plot
    def distPlot():
        fig, ax = plt.subplots()
        ax.hist(waiting, bins=input.bins(), color="darkgray", edgecolor="white")
        ax.set_xlabel("Waiting time to next eruption (in mins)")
        ax.set_title("Histogram of waiting times")
        return fig


app = App(app_ui, server)
