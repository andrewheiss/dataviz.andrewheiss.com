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
THEME = 'theme'

# Folder where everything lives
PATH = 'content'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# STATIC_PATHS = ['.htaccess', 'favicon.ico', 'robots.txt', 'files',
#                 'googlee5d783d34e81df8c.html']
READERS = {'html': None}  # Don't parse HTML files

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pandoc_reader', 'extract_toc']

PANDOC_ARGS = [
    '-t', 'html5',
    '--smart',
    '--base-header-level=1',
    '--filter', 'pandoc-sidenote',
    '--section-divs',  # wrap heading blocks with <section>
    '--table-of-contents',
    '--template=theme/pandoc-templates/tufte.html5'
]

PANDOC_EXTENSIONS = [
    '-markdown_in_html_blocks',
    '+raw_html'
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
             ('Reference', '/reference/')]


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
