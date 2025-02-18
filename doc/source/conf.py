# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = 'documents'
copyright = '2025, Danys'
author = 'Danys'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, os.path.abspath('../../Semana_8_documentacion_y_mantenimiento'))  # Para que Sphinx encuentre el código

extensions = [
    'sphinx.ext.autodoc',  # Permite extraer docstrings
    'sphinx.ext.napoleon', # Para soportar Google y NumPy docstrings
    'sphinx.ext.viewcode'
]

autodoc_mock_imports = []  # Agrega módulos externos si es necesario

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


