# -*- coding: utf-8 -*-
#
# This file is execfile() with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import importlib
import os
import sys
import inspect
import re
import glob


from datetime import datetime
CURRENT_YEAR = datetime.now().year
START_YEAR = 2015

DEV_YEARS = '{}'.format(START_YEAR) if START_YEAR == CURRENT_YEAR else '{}-{}'.format(START_YEAR, CURRENT_YEAR) 
# General information about the project.

PATH0 = os.path.join(os.path.abspath(os.path.pardir), 'src')
PACKAGE_NAME = 'nvector'
project = u'nvector'
author = 'Kenneth Gade and Per A. Brodtkorb'
organizations = 'Norwegian Defence Research Establishment (FFI)'
copyright = ', '.join((DEV_YEARS, organizations))

__location__ = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(__location__, '../src/.'))

# -- Run sphinx-apidoc ------------------------------------------------------
# This hack is necessary since RTD does not issue `sphinx-apidoc` before running
# `sphinx-build -b html . _build/html`. See Issue:
# https://github.com/rtfd/readthedocs.org/issues/1139
# DON'T FORGET: Check the box "Install your project inside a virtualenv using
# setup.py install" in the RTD Advanced Settings.
# Additionally it helps us to avoid running apidoc manually

#
#from sphinx import apidoc
#
#output_dir = os.path.join(__location__, "api")
#module_dir = os.path.join(__location__, "../src", PACKAGE_NAME)
#try:
#    shutil.rmtree(output_dir)
#except Exception:
#    pass
#cmd_line_template = "sphinx-apidoc -f -o {outputdir} {moduledir}"
#cmd_line = cmd_line_template.format(outputdir=output_dir, moduledir=module_dir)
#apidoc.main(cmd_line.split(" "))



# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.autosummary',
              'sphinx.ext.viewcode',
              'sphinx.ext.coverage',
              'sphinx.ext.ifconfig',
              'sphinx.ext.imgmath',
              'numpydoc',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
PACKAGE = importlib.import_module(PACKAGE_NAME, './src')

# The full version, including alpha/beta/rc tags.
release = PACKAGE.__version__

#
# The short X.Y version
version = re.sub(r'(\d+\.\d+)\.\d+(.*)', r'\1\2', release)
version = re.sub(r'(\.dev\d+).*?$', r'\1', version)
print("{0!s} {1!s}".format(version, release))


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.

language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'tests']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# supress warnings from the numpydoc extension,
numpydoc_show_class_members = False

# Make numpydoc to generate plots for example sections
numpydoc_use_plots = True

# If numfig is true, figures, tables and code-blocks are automatically numbered if
# they have a caption. The numref role is enabled. Obeyed so far only by
# HTML and LaTeX builders. Default is False.
numfig = True
# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

autosummary_generate = glob.glob("api/*.rst")


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme' # 'alabaster'
# If true, the index is generated twice: once as a single page with all the entries, and once as one page per starting letter. Default is False.
html_split_index = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = True

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#
# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'donate.html',
#     ]
# }

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = PACKAGE_NAME + 'doc'


# -- Options for LaTeX output
# Documents to append as an appendix to all manuals.
#latex_appendices = ['appendix/changelog',
#                    'appendix/authors',
#                    'appendix/license',
#                    'appendix/acknowledgement',
#                    'appendix/bibliography']

# If false, no module index is generated.
#
latex_domain_indices = True

# latex_engine = 'xelatex'
latex_engine = 'pdflatex'


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,  '{}-{}.tex'.format(PACKAGE_NAME, release), project + ' Documentation',
     author, 'manual'),
]

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': '',
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'user_guide.tex', u'nvector Documentation',
     u'Kenneth Gade and Per A Brodtkorb', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = ""

# If true, show page references after internal links.
latex_show_pagerefs = True
# If true, show URL addresses after external links.
latex_show_urls = 'footnote'  # 'no', 'inline'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
latex_use_parts = True
# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False



# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, PACKAGE_NAME, project + ' Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, PACKAGE_NAME, project + ' Documentation',
     author, PACKAGE_NAME, 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']