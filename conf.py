# Minimal Sphinx configuration file for Read the Docs
# Since we use pre-built HTML, this file is just to satisfy Read the Docs requirements

project = 'Galyst'
copyright = '2025, Shuai Lu'
author = 'Shuai Lu'

# Minimal extension configuration
extensions = []

# HTML output configuration
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# Tell Sphinx to use our already built HTML
html_build_dir = '.'