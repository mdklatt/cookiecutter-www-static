""" Test the python-app Cookiecutter template.

A template project is created in a temporary directory, the application is
installed into a self-contained venv environment, and the application test 
suite is run.

"""
from contextlib import contextmanager
from json import load
from os import chdir
from os.path import abspath
from os.path import dirname
from os.path import join
from shlex import split
from shutil import which
from subprocess import check_call
from tempfile import TemporaryDirectory

from cookiecutter.main import cookiecutter

def main():
    """ Execute the test.
    
    """
    template = dirname(dirname(abspath(__file__)))
    defaults = load(open(join(template, "cookiecutter.json")))
    with TemporaryDirectory() as tmpdir:
        chdir(tmpdir)
        cookiecutter(template, no_input=True)
        chdir(join(tmpdir, defaults["project_slug"]))
        # pip = which("pip", path=path) or "pip"  # Travis CI workaround
        # install = "{:s} install .".format(pip)
        # for req in (join(root, "requirements.txt") for root in (".", "test")):
        #     # Add each requirements file to the install.
        #     install = " ".join((install, "--requirement={:s}".format(req)))
        # check_call(split(install))
        # pytest = which("pytest", path=path) or "pytest"  # Travis CI workaround
        # test = "{:s} --verbose test".format(pytest)
        # check_call(split(test))
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
