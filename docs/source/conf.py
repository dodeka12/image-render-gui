# <LICENSE id="CC BY-SA 4.0">
#
#
#   Functional JSON module documentation
#   Copyright 2022 Robert Bosch GmbH and its subsidiaries
#
#   This work is licensed under the
#
#       Creative Commons Attribution-ShareAlike 4.0 International License.
#
#   To view a copy of this license, visit
#       http://creativecommons.org/licenses/by-sa/4.0/
#   or send a letter to
#       Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
#
#
# </LICENSE>
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import json
from pathlib import Path
from catharsys.setup.module import GetRepoVersion

pathModule = Path(__file__).parent.parent.parent
sVersion = GetRepoVersion(pathModule=pathModule)

pathSetup = pathModule.parent.parent
pathDocsSrcMain = pathSetup / "docs" / "source"

# -- Project information -----------------------------------------------------

project = "Catharsys Web GUI"
copyright = "2023, Robert Bosch GmbH"
author = "Christian Perwass"

# The full version, including alpha/beta/rc tags
release = sVersion


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    ## if myst_nb is included, don't include 'myst_parser'
    "myst_parser",
    # "myst_nb",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "dollarmath",
    "html_image",
]

myst_substitutions = {"ProjectName": project}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


intersphinx_mapping = {}

pathConfig = pathDocsSrcMain / "auto_config.json"
if pathConfig.exists():
    with pathConfig.open("r") as xFile:
        dicConfig = json.load(xFile)
    # endwith

    lModules = dicConfig["lModules"]
    for sModule in lModules:
        intersphinx_mapping[sModule] = (
            f"../../{sModule}/html",
            f"../../../../docs/build/{sModule}/html/objects.inv",
        )
    # endfor
    
    intersphinx_mapping["image-render-setup"] = (
        "../../html",
        "../../../../docs/build/html/objects.inv",
    )
# endif
