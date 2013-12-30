#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom Dong'
SITENAME = u'Minga Demo'
SITEURL = 'localhost:8000'

TIMEZONE = 'Europe/Paris'

LOCALE = (
	'chn', 'usa',  					# On Windows
    'zh_CN.UTF-8', 'en_US.UTF-8'    # On Unix/Linux
)

DATE_FORMATS = {
    'en': '%Y-%m-%d',
    'zh': '%Y-%m-%d',
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'

THEME = 'pelican-minga'
OUTPUT_PATH = '../'

TAGS_URL = '/tags'
TAGS_SAVE_AS = 'tags/index.html'

ARCHIVES_URL = '/archive'
ARCHIVES_SAVE_AS = 'archive/index.html'

ENABLE_MATHJAX = True
DOCUTILS_SETTINGS = {'math_output':'MathJax'}

GITHUB_URL = 'https://github.com/tomtung'
TWITTER_URL = 'https://twitter.com/tomtung'
DOUBAN_URL = 'http://www.douban.com/people/tomtung'
WEIBO_URL = 'http://www.weibo.com/1245986775'
