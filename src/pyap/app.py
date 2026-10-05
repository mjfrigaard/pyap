from shiny import App, ui, render, run_app
import matplotlib.pyplot as plt

from pyap.data import geyser_waiting

waiting = geyser_waiting()

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


def run() -> None:
    """Launch the pyap Shiny app in a browser."""
    run_app("pyap.app:app", launch_browser=True)
