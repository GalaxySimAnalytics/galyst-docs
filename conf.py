# Minimal configuration for static HTML

project = 'Galyst'
copyright = '2025, Shuai Lu'
author = 'Shuai Lu'
version = '0.1.0'
release = '0.1.0'

# Do not use any extensions
extensions = []

# Simplest HTML theme
html_theme = 'sphinx_book_theme'

html_static_path = ['_static']

html_copy_source = False
html_show_sourcelink = False

# Main document
master_doc = 'index'
root_doc = 'index'  # For newer Sphinx versions