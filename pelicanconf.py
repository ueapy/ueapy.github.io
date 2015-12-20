#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Group'
SITENAME = u'Python Group UEA'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['pdfs', 'figures', 'extra/favicon.ico', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'extra/custom.css'}
}
CUSTOM_CSS = 'extra/custom.css'

THEME = '../modified-bootstrap3'
BOOTSTRAP_THEME = 'yeti'
PYGMENTS_STYLE = 'friendly'
OVERWRITE_NB_HEADER = False

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['liquid_tags.notebook','tag_cloud','summary']

NOTEBOOK_DIR = 'notebooks'

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
SHOW_ARTICLE_CATEGORY = False
SHOW_ARTICLE_AUTHOR = True
DISPLAY_CATEGORIES_ON_MENU = False
#SOCIAL = (('github', 'http://github.com/ueapy'))

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('EarthPy', 'http://earthpy.org/'),
         ('Python4Oceanographers', 'https://ocefpaf.github.io/python4oceanographers/'),
         ('PyAOS', 'http://pyaos.johnny-lin.com/'),
         ('PyHOGs', 'http://pyhogs.github.io/'),
         ('Pythonic Perambulations', 'https://jakevdp.github.io/'),
         ('Meteodenny', 'http://dennissergeev.github.io/'),
         )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sharing
GITHUB_URL = 'https://github.com/ueapy'
DISQUS_SITENAME = 'pythonuea'
ADDTHIS_PROFILE = "ra-564e4d3ff0b9f071"
FACEBOOK_LIKE = True
GOOGLE_PLUS_ONE = True
GOOGLE_CUSTOM_SEARCH_SIDEBAR = False
