#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Group'
SITENAME = u'Python Group UEA'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['robots.txt', 'pdfs', 'figures', 'extra/favicon.ico', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'extra/custom.css'}
}
CUSTOM_CSS = 'extra/custom.css'

THEME = '../pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'cosmo'
PYGMENTS_STYLE = 'default'
OVERWRITE_NB_HEADER = True
EXTRA_HEADER = open('_nb_header.html').read()

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['tag_cloud', 'summary', 'i18n_subsites',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

NOTEBOOK_DIR = 'notebooks'

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
SHOW_ARTICLE_CATEGORY = False
SHOW_ARTICLE_AUTHOR = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
#MENUITEMS = [
#             ('Python Course 2016',
#              'https://ueapy.github.io/enveast_python_course/'),
#             ('Meetings calendar', 'https://ueapy.github.io/meetings-calendar.html'),
#             ('Ideas for meetings', 'https://ueapy.github.io/meetings-ideas.html'),
#             #  ('Archives', '/archives.html')
#            ]
# SOCIAL = (('github', 'http://github.com/ueapy'))

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python Course 2016', 'https://ueapy.github.io/enveast_python_course/'),
         ('Learn Python online', 'http://bafflednerd.com/learn-python-online'),
         ('Python Videos', 'http://pyvideo.org/'),
         ('From Python to Numpy', 'http://www.labri.fr/perso/nrougier/from-python-to-numpy/'),
         ('EarthPy', 'http://earthpy.org/'),
         ('Python4Oceanographers',
          'https://ocefpaf.github.io/python4oceanographers/'),
         ('PyAOS', 'http://pyaos.johnny-lin.com/'),
         ('PyHOGs', 'http://pyhogs.github.io/'),
         ('Pythonic Perambulations', 'https://jakevdp.github.io/'),
         ('Meteodenny', 'https://dennissergeev.github.io/'),
         )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Sharing
GITHUB_URL = 'https://github.com/ueapy'
DISQUS_SITENAME = 'pythonuea'
ADDTHIS_PROFILE = "ra-564e4d3ff0b9f071"
FACEBOOK_LIKE = True
GOOGLE_PLUS_ONE = True
GOOGLE_CUSTOM_SEARCH_SIDEBAR = False
