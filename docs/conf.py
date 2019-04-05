# -*- coding: utf-8 -*-

import os
import sys

# -- General configuration ------------------------------------------------
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Bartacus'
copyright = u'Emily Karisch'
author = u'Emily Karisch'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'2.0'
# The full version, including alpha/beta/rc tags.
release = u'2.0.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'INSTALL-ME.md']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
# The name for this set of Sphinx documents.
html_title = u'Bartacus Documentation'

# A shorter title for the navigation bar.
html_short_title = u'Bartacus'

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# -- Options for Intersphinx ----------------------------------------------
intersphinx_mapping = {
    'bundle': ('https://bartacus.readthedocs.io/projects/bundle/en/stable/', None),
    'platformsh-bundle': ('https://bartacus.readthedocs.io/projects/platformsh-bundle/en/stable/', None),
    'twig-bundle': ('https://bartacus.readthedocs.io/projects/twig-bundle/en/stable/', None),
}
