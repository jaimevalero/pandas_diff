import pandas_diff

project = "pandas_diff"
copyright = "2021-2026, Jaime Valero"
author = "Jaime Valero"
version = pandas_diff.__version__
release = pandas_diff.__version__

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
