#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fer Rios'
SITENAME = u'ferztyle'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Asuncion'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SHOW_ARTICLE_AUTHOR = True
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/')
#         )


# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/ferztyle/pelican-themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['/home/ferztyle/pelican-plugins'] 
PLUGINS = ['i18n_subsites', 'tipue_search']
BOOTSTRAP_THEME = 'cosmo'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU  = True

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

I18N_SUBSITES = {
    'es': {
        'SITENAME': 'Fer blog',
        }
    }


#GITHUB_URL = ''
#TWITTER_URL = 'https://twitter.com/Ferztyle'
#FACEBOOK_URL = ''

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

#DISPLAY_ARCHIVE_ON_SIDEBAR = True
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

SOCIAL = (('twitter', 'http://twitter.com/ferztyle'),
          ('linkedin', 'www.linkedin.com/in/ferrios'))

