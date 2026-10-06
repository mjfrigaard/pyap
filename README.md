<h1 align="center"> <code>pyap</code> </h1>

<h3 align="center"> Code examples for Shiny for Python App-Packages </h3>

<hr>

# pyap

`pyap` provides code examples demonstrating how to build and package a [Shiny for Python](https://shiny.posit.co/py/) application as a proper Python package, using [`uv`](https://docs.astral.sh/uv/) for environment management and [`pytest`](https://docs.pytest.org/) for testing.

## Movie review data application

The original code and data for the Shiny app comes from the [Building Web Applications with Shiny](https://rstudio-education.github.io/shiny-course/) course.

## Using code examples

Each branch contains the app at a specific stage of development.

```bash
git clone https://github.com/mjfrigaard/pyap.git
cd pyap
git checkout <branch_name>
```

Install the Python version and dependencies listed in `pyproject.toml` (uv creates the `.venv/` folder and `uv.lock` for us):

```bash
uv sync
```

Run the app with:

```bash
uv run shiny run app.py
```

## Branches

| Branch | Description |
|--------|-------------|
| `01_whole-game` | Whole game: `app.py` to an installable package (`src/` layout, `uv`, `pytest`, `run()`) |
| `02.1_shiny-app` | Default "Hello Shiny" template |
| `02.2_movies-app` | Movies scatter plot app |
| `02.3_proj-app` | App with project structure |
| `03.1_pyproject` | Add `pyproject.toml` metadata and dependencies |
| `03.2_uv` | uv environment management |
