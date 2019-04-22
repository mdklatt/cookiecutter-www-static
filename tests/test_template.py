""" Test the python-app Cookiecutter template.

A template project is created in a temporary directory, the application is
installed into a self-contained venv environment, and the application test 
suite is run.

"""
from json import loads
from os import chdir
from pathlib import Path
from shlex import split
from subprocess import check_call
from tempfile import TemporaryDirectory

from cookiecutter.main import cookiecutter


def main():
    """ Execute the test.
    
    """
    template = Path(__file__).resolve().parents[1]
    defaults = loads(template.joinpath("cookiecutter.json").read_text())
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        cookiecutter(str(template), no_input=True, output_dir=str(tmpdir))
        chdir(str(tmpdir.joinpath(defaults["project_slug"])))
        for command in "install", "run-script typescript", "run-script test":
            check_call(split(f"npm {command:s}"))
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
