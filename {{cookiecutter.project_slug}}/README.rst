{% set delim = "#" * cookiecutter.www_name|length -%}
{{ delim }}
{{ cookiecutter.www_name }}
{{ delim }}

This is the {{ cookiecutter.www_name }} web site.


====================
Development Workflow
====================

.. _Node.js: https://nodejs.org

The development machine must have `Node.js`_ installed.


Install NPM packages:

.. code-block:: console

  $ npm install


Build TypeScript source; output will be in ``static/script``:

.. code-block:: console

  $ npm typescript


Run tests:

.. code-block:: console

  $ npm test
