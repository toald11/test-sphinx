# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-test'
copyright = '2026, toald11'
author = 'toald11'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

numfig = True

language = 'ja'

extensions.append("sphinxcontrib.plantuml")
plantuml = 'java -jar /usr/local/bin/plantuml.jar -config /usr/local/share/jp.pu'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
templates_path = ["_template"]
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/regular.min.css",
]
html_theme_options = {}
html_theme_options["light_css_variables"] = {
    "color-brand-primary": "#CC6600",
    "color-brand-content": "#CCCC99"
}
html_theme_options["dark_css_variables"] = {
    "color-brand-primary": "#FFBB00",
    "color-brand-content": "#FFFF99"
}
html_theme_options["sidebar_hide_name"] = True
html_theme_options["navigation_with_keys"] = True
html_theme_options["top_of_page_buttons"] = ["view", "edit"]
html_theme_options["announcement"] = "furo themeは<em>html_theme_options</em>でページ全体の通知を設定できる。"
html_theme_options["light_logo"] = "icon_light.png"
html_theme_options["dark_logo"] = "icon_dark.png"
pdf_icon = {
    "name": "PDF",
    "url": "https://toald11.github.io/test-sphinx/test.pdf",
    "html": "",
    "class": "fa-regular fa-file-pdf fa-2x",
}
github_icon = {
    "name": "GitHub",
    "url": "https://github.com/toald11/test-sphinx",
    "html": "",
    "class": "fa-brands fa-github fa-2x",
}
html_theme_options["footer_icons"] = [
    pdf_icon,
    github_icon,
]
# html_theme_options["source_repository"] = "https://github.com/toald11/test-sphinx"
# html_theme_options["source_branch"] = "main"
# html_theme_options["source_directory"] = "source/"

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        # "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

html_title = "sphinxメモ"