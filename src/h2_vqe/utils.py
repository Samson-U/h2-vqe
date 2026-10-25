from pathlib import Path


# Project root: the folder containing pyproject.toml
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
RESULTS_DIR = PROJECT_ROOT / "results"
DOCS_DIR = PROJECT_ROOT / "docs"


def ensure_project_directories():
    """Create the standard output and data directories if needed."""
    for directory in (RAW_DATA_DIR, RESULTS_DIR, DOCS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def get_results_path(filename):
    """Return the path for a file saved in the results directory."""
    if Path(filename).name != filename:
        raise ValueError("Please provide a filename, not a directory path.")

    return RESULTS_DIR / filename
