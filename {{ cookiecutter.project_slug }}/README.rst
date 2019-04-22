{% set delim = "#" * cookiecutter.app_name|length -%}
{{ delim }}
{{ cookiecutter.app_name }}
{{ delim }}

This is the {{ cookiecutter.app_name }} application.


====================
Minimum Requirements
====================


=====================
Optional Requirements
=====================


===========
Basic Setup
===========

Install for the current user:

.. code-block:: console

  $ python setup.py install --user


Run the application:

.. code-block:: console

  $ python -m {{ cookiecutter.app_name }} --help


Run the test suite:

.. code-block:: console
   
  $ pytest test/


Build documentation:

.. code-block:: console

  $ sphinx-build -b html doc doc/_build/html
