#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import glob

# Basic config
AUTHOR = 'Daniel S. Standage'
SITENAME = 'Daniel Standage'
TIMEZONE = 'America/Indiana/Indianapolis'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
FOOTER_YEARS = '2015-2016'

PATH = 'content'
THEME = 'bootstrap'
SITEURL = 'http://standage.github.io'
RELATIVE_URLS = True
DEFAULT_PAGINATION = 10
CACHE_CONTENT = False
DISQUS_SITENAME = 'standage-github-io'
SUMMARY_MAX_LENGTH = 60

# Blog/page/category config
IGNORE_FILES = ['.ipynb_checkpoints']
DISPLAY_CATEGORIES_ON_MENU = False
INDEX_SAVE_AS = 'notebook.html'
PAGE_ORDER_BY = 'navorder'

# Settings for left side well
ADDRESS = ('205A Simon Hall',
           'Indiana University',
           '212 South Hawthorne Drive',
           'Bloomington, IN 47405')

# Affiliations (replaced "Blogroll" in theme)
LINKS = (('Brendel Group', 'http://brendelgroup.org/'),
         ('Toth Lab', 'http://www.public.iastate.edu/~amytoth/Toth_lab/Home.html'),
         ('Indiana Biology Department', 'http://www.bio.indiana.edu/'),
         ('Iowa State BCB Program', 'http://www.bcb.iastate.edu/'),)

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
