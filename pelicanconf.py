import os
import pathlib
from functools import partial

PATH = '.'
OUTPUT_PATH = pathlib.Path('~/hrbatypes').expanduser()

SITENAME = 'VSK MFF UK BL'
SITEURL = os.environ.get('URL', '')

CSS_DEBUG = os.environ.get('CSS_DEBUG', '').lower() in {'1', 'true', 'yes', 'on'}

ARTICLE_URL = PAGE_URL = '{slug}/'
ARTICLE_SAVE_AS = PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'sezony/{slug}/'
CATEGORY_SAVE_AS = 'sezony/{slug}/index.html'

ARCHIVES_SAVE_AS = AUTHOR_SAVE_AS = AUTHORS_SAVE_AS = CATEGORIES_SAVE_AS = TAGS_SAVE_AS = ''

SLUG_REGEX_SUBSTITUTIONS = [
    (r'[^\w\s/.-]', ''),
    (r'[\s/.-]+', '-'),
    (r'^-', ''),
    (r'-$', ''),
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.nl2br': {},
    },
    'output_format': 'html5',
}

DEFAULT_LANG = 'cs'
LOCALE = 'cs_CZ.utf8'
DEFAULT_DATE_FORMAT = '%A, %-d. %B %Y, %H:%M'

TIMEZONE = 'Europe/Prague'

STATIC_PATHS = ['favicon.ico', 'static']
STATIC_CREATE_LINKS = True

THEME = 'theme'
TEMPLATE_EXTENSIONS = ['.html.jinja', '.html']

ARTICLE_EXCLUDES = ['theme']
IGNORE_FILES = ['README.md']

FEED_RSS = 'rss.xml'
FEED_MAX_ITEMS = 10

FEED_ALL_ATOM = CATEGORY_FEED_ATOM = AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = TRANSLATION_FEED_ATOM = None


def get_article_key(article):
    sticky = getattr(article, 'sticky', '0')
    return bool(int(sticky)), article.date


JINJA_FILTERS = {
    'sort_articles': partial(sorted, key=get_article_key, reverse=True),
}
