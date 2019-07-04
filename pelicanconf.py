import os
from functools import partial

PATH = '.'
PORT = 9999

SITENAME = 'VSK MFF UK BL'
SITEURL = os.environ.get('URL', '')

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

ARTICLE_EXCLUDES = ['output', 'theme']
IGNORE_FILES = ['README.md']

FEED_RSS = 'rss.xml'
FEED_MAX_ITEMS = 10

FEED_ALL_ATOM = CATEGORY_FEED_ATOM = AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = TRANSLATION_FEED_ATOM = None


def get_category_key(category):
    name = category[0].name
    if name.startswith('Léto'):
        return 0, name
    elif name.startswith('Zima'):
        return -1, name
    else:
        return -2, name


def get_article_key(article):
    sticky = getattr(article, 'sticky', '0')
    return bool(int(sticky)), article.date


def postprocess_content(content, smaller_headers=False):
    content = content.replace('<table>', '<table class="table table-striped">')
    content = content.replace('<h2>Přílohy:</h2>', '<h2 class="h4 mb-1">Přílohy:</h2>')
    if smaller_headers:
        content = content.replace('<h2>', '<h2 class="h3">')
        content = content.replace('<h3>', '<h3 class="h4">')
    return content


JINJA_FILTERS = {
    'sort_categories': partial(sorted, key=get_category_key, reverse=True),
    'sort_articles': partial(sorted, key=get_article_key, reverse=True),
    'postprocess_content': postprocess_content,
}
