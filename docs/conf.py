from pallets_sphinx_themes import get_version
from pallets_sphinx_themes import ProjectLink

# Project --------------------------------------------------------------

project = "Werkzeug"
copyright = "2007 Pallets"
author = "Pallets"
release, version = get_version("Werkzeug")

# General --------------------------------------------------------------

default_role = "code"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "pallets_sphinx_themes",
]
autoclass_content = "both"
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_preserve_defaults = True
extlinks = {
    "issue": ("https://github.com/pallets/werkzeug/issues/%s", "#%s"),
    "pr": ("https://github.com/pallets/werkzeug/pull/%s", "#%s"),
    "ghsa": ("https://github.com/advisories/GHSA-%s", "GHSA-%s"),
}
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

# HTML -----------------------------------------------------------------

html_theme = "werkzeug"
html_theme_options = {"index_sidebar_logo": False}
html_context = {
    "project_links": [
        ProjectLink("Donate", "https://palletsprojects.com/donate"),
        ProjectLink("PyPI Releases", "https://pypi.org/project/Werkzeug/"),
        ProjectLink("Source Code", "https://github.com/pallets/werkzeug/"),
        ProjectLink("Issue Tracker", "https://github.com/pallets/werkzeug/issues/"),
        ProjectLink("Chat", "https://discord.gg/pallets"),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html", "ethicalads.html"]}
html_static_path = ["_static"]
html_favicon = "_static/werkzeug-icon.svg"
html_logo = "_static/werkzeug-logo.svg"
html_title = f"Werkzeug Documentation ({version})"
html_show_sourcelink = False
