project = 'aaa'
copyright = '2022'
author = 'KV'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgmath', 
    'sphinx.ext.todo',
    'breathe',
]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'haiku' # 'alabaster'

templates_path = [
    "_templates",
]

html_sidebars = [
    "versioning.html",
]

import subprocess
subprocess.call('make clean', shell=True)
subprocess.call('cd ../../doxygen ; doxygen', shell=True)

breathe_projects = { "aaa": "../../doxygen/build/xml/" }
breathe_default_project = "aaa"
