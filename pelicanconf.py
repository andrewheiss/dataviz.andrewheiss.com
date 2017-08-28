#!/usr/bin/env python3

# ------------------
# Site information
# ------------------
AUTHOR = 'Andrew Heiss'
SITENAME = 'Data Visualization'
COURSE_NUMBER = 'MPA 635'
SITEURL = ''
DESCRIPTION = ''

PATH = 'content'

TIMEZONE = 'America/Denver'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = 'en'

TYPOGRIFY = False


# ---------------
# Site building
# ---------------
DELETE_OUTPUT_DIRECTORY = True

# Theme
THEME = '/Users/andrew/Development/•Pelican/themes/ath-tufte'

# Folder where everything lives
PATH = 'content'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# STATIC_PATHS = ['.htaccess', 'favicon.ico', 'robots.txt', 'files',
#                 'googlee5d783d34e81df8c.html']
READERS = {'html': None}  # Don't parse HTML files

RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figures/'}
RMD_READER_CLEANUP = True
STATIC_PATHS = ['figures', 'images']

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_toc', 'pandoc_reader', 'rmd_pandoc_reader']
# rmd_reader (or rmd_pandoc_reader) should come last:
# https://github.com/getpelican/pelican-plugins/tree/master/rmd_reader

PANDOC_ARGS = [
    '-t', 'html5',
    '--smart',
    '--highlight-style', 'haddock',
    '--base-header-level=2',
    '--filter', 'pandoc-sidenote',
    '--section-divs',  # wrap heading blocks with <section>
    '--template=' + THEME + '/pandoc-templates/tufte.html5'
]

PANDOC_EXTENSIONS = [
    '+markdown_in_html_blocks',
    '+raw_html',
]

# No feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# None of these pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''


# ------------
# Site items
# ------------
MENUITEMS = [('Syllabus', '/syllabus/'),
             ('Schedule', '/schedule/'),
             ('Assignments', '/assignments/'),
             ('Reference', '/reference/'),
             ('Rmd test', '/testing/')]

ATH_TUFTE_ICON = "/images/course-icon.png"
ATH_LINK_COLOR = "#A5452B"
ATH_LINK_HOVER_COLOR = "#ECAD49"


# ---------------
# Jinja filters
# ---------------
import jinja2
import os

# Get the final basename or directory name of a path
def get_slug(url):
    slug = os.path.basename(os.path.dirname(url))
    return slug

JINJA_FILTERS = {'get_slug': get_slug}
