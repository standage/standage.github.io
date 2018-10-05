#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import glob

# Basic config
AUTHOR = 'Daniel S. Standage'
SITENAME = 'Daniel S. Standage'
TIMEZONE = 'US/Eastern'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
FOOTER_YEARS = '2015-2018'

PATH = 'content'
THEME = 'bootstrap'
SITEURL = 'http://standage.github.io'
RELATIVE_URLS = True
DEFAULT_PAGINATION = 10
CACHE_CONTENT = False
DISQUS_SITENAME = 'standage-github-io'
SUMMARY_MAX_LENGTH = 60

# Disallow indexing of drafts
STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Blog/page/category config
IGNORE_FILES = ['.ipynb_checkpoints']
DISPLAY_CATEGORIES_ON_MENU = False
INDEX_SAVE_AS = 'notebook.html'
PAGE_ORDER_BY = 'navorder'

# Settings for left side well
ADDRESS = ('Assoc. Principal Investigator,',
           'Bioinformatics',
           'NBACC')

# Affiliations (replaced "Blogroll" in theme)
LINKS = (('Lab for Data Intensive Biology', 'http://ivory.idyll.org/lab/'),
         ('Brendel Group', 'http://brendelgroup.org/'),
         ('Toth Lab', 'http://www.public.iastate.edu/~amytoth/Toth_lab/Home.html'),)


# Social widget
SOCIAL = (('GitHub', 'http://github.com/standage'),
          ('Twitter', 'https://twitter.com/byuhobbes'),
          ('StackExchange', 'http://stackexchange.com/users/208980/daniel-standage?tab=accounts'))

# Feed settings
FEED_ALL_RSS = 'feed.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugin config
PLUGIN_PATHS = ['plugins']
PLUGINS = ['ipynb']
IPYNB_USE_META_SUMMARY = True
