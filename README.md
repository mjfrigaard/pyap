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

Create a virtual environment and install dependencies with [`uv`](https://docs.astral.sh/uv/):

```bash
uv venv .venv
```

```bash
uv pip install -r requirements.txt
```

Run any branch with:

```bash
shiny run app.py
```

## Branches

| Branch | Description |
|--------|-------------|
| `02.1_shiny-app` | Default "Hello Shiny" template |
| `02.2_movies-app` | Movies scatter plot app |
| `02.3_proj-app` | App with project structure |
| `03.1_pyproject` | Add `pyproject.toml` metadata |
| `03.2_uv` | uv environment management |
| `03.3_create-package` | Full Python package structure |
| `04_uv` | Editable install with uv |
| `05_docstrings` | Docstrings on all public functions |
| `06.1_exports` | `__init__.py` explicit exports |
| `06.2_imports` | Package dependencies |
| `07_data` | Data as package resource |
| `08_run` | `run()` function + `__main__.py` |
| `09_www` | Static resources |
| `10_debugger` | debugpy integration |
| `11_debug-print` | Debug printing patterns |
| `12.1_debug-mods` | Debugging Shiny modules |
| `12.2_mod-comms` | Module communication with `reactive.Value` |
| `13_logging` | Python `logging` module |
| `14_tests_suite` | pytest test suite |
| `15_specs` | Test specifications |
| `16.1_test-help` | pytest fixtures |
| `16.2_test-data` | Test data |
| `16.3_test-logger` | Test logging |
| `16.4_test-snapshots` | Playwright snapshot tests |
| `17_test-modules` | Testing Shiny modules |
| `18_test-system` | System / integration tests |
| `19_connect` | Posit Connect deployment |
| `20_docker` | Docker deployment |
| `21.1_gha-style` | GitHub Actions linting |
