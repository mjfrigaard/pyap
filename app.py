# Run with: shiny run app.py

from shiny import App, ui, render, reactive
import pandas as pd

from utils import scatter_plot

movies = pd.read_csv("movies.csv")

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            "y",
            "Y-axis:",
            choices={
                "imdb_rating": "IMDB rating",
                "imdb_num_votes": "IMDB number of votes",
                "critics_score": "Critics Score",
                "audience_score": "Audience Score",
                "runtime": "Runtime",
            },
            selected="audience_score",
        ),
        ui.input_select(
            "x",
            "X-axis:",
            choices={
                "imdb_rating": "IMDB rating",
                "imdb_num_votes": "IMDB number of votes",
                "critics_score": "Critics Score",
                "audience_score": "Audience Score",
                "runtime": "Runtime",
            },
            selected="critics_score",
        ),
        ui.input_select(
            "z",
            "Color by:",
            choices={
                "title_type": "Title Type",
                "genre": "Genre",
                "mpaa_rating": "MPAA Rating",
                "critics_rating": "Critics Rating",
                "audience_rating": "Audience Rating",
            },
            selected="mpaa_rating",
        ),
        ui.input_slider("alpha", "Alpha:", min=0.0, max=1.0, value=0.4, step=0.05),
        ui.input_slider("size", "Size:", min=1, max=5, value=3),
        ui.input_text(
            "plot_title",
            "Plot title",
            placeholder="Enter text to be used as plot title",
        ),
        ui.input_action_button("update_plot_title", "Update plot title"),
    ),
    ui.p(
        "These data were obtained from ",
        ui.a("IMDB", href="http://www.imdb.com/"),
        " and ",
        ui.a("Rotten Tomatoes", href="https://www.rottentomatoes.com/"),
        ".",
    ),
    ui.p(
        f"The data represent {len(movies)} randomly sampled movies "
        "released between 1972 to 2014 in the United States."
    ),
    ui.output_plot("scatterplot"),
    ui.hr(),
    ui.p(
        ui.em(
            "The code for this Shiny application comes from ",
            ui.a(
                "Building Web Applications with Shiny",
                href="https://rstudio-education.github.io/shiny-course/",
            ),
        )
    ),
)


def server(input, output, session):
    # only updates title when button is clicked, runs on init with empty string
    @reactive.calc
    @reactive.event(input.update_plot_title, ignore_none=False, ignore_init=False)
    def new_plot_title():
        return input.plot_title().title()

    @render.plot
    def scatterplot():
        return scatter_plot(
            df=movies,
            x_var=input.x(),
            y_var=input.y(),
            col_var=input.z(),
            alpha_var=input.alpha(),
            size_var=input.size(),
            title=new_plot_title(),
        )


app = App(app_ui, server)
