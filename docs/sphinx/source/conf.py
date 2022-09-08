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
    "sphinx_multiversion",
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

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = None

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = 'version/{config.release}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False

import subprocess
subprocess.call('make clean', shell=True)
subprocess.call('cd ../../doxygen ; doxygen', shell=True)

breathe_projects = { "aaa": "../../doxygen/build/xml/" }
breathe_default_project = "aaa"
