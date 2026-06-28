# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath("./rozdzial_5"))

project = 'Sprawozdanie z laboratorium bazy danych'
copyright = '2026, Kamil Lewandowski 284368'
author = 'Kamil Lewandowski 284368'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
]

autodoc_mock_imports = [
    "pandas",
    "sqlalchemy",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

# -- Options for LaTeX/PDF output -------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
}
