<h1 align="center"> <code>pyap</code> </h1>

<h3 align="center"> Code examples for Shiny for Python App-Packages </h3>

<hr>

# pyap

`pyap` provides code examples demonstrating how to build and package a [Shiny for Python](https://shiny.posit.co/py/) application as a proper Python package, using [`uv`](https://docs.astral.sh/uv/) for environment management and [`pytest`](https://docs.pytest.org/) for testing.

## Using code examples

Each branch contains the app at a specific stage of development.

```bash
git clone https://github.com/mjfrigaard/pyap.git
cd pyap
git checkout <branch_name>
```

Create and activate a virtual environment (the `.venv/` folder isn't tracked by Git, so it carries over when you switch branches):

```bash
uv venv
source .venv/bin/activate
```

Install the packages the app imports:

```bash
uv pip install shiny matplotlib numpy
```

Run the app with:

```bash
shiny run app.py
```

## Branches

| Branch | Description |
|--------|-------------|
| `01_whole-game` | Whole game: `app.py` to an installable package (`src/` layout, `uv`, `pytest`, `run()`) |
| `02.1_shiny-app` | Default "Hello Shiny" template |
