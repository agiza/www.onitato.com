#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Justin Phelps'
SITENAME = u"Linuturk's Natter"
SITEURL = 'http://www.onitato.com'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'
DEFAULT_PAGINATION = 5
GITHUB_URL = 'https://github.com/Linuturk/www.onitato.com'

# Blogroll
LINKS = (('Request a Topic', 'https://github.com/Linuturk/www.onitato.com/issues'),
         ('Report an Issue', 'https://github.com/Linuturk/www.onitato.com/issues'),
         ('Donate Bitcoin', 'http://linuturk.tip.me/'))

# Social widget
SOCIAL = (('google+', 'https://plus.google.com/+JustinPhelpsLinuturk/posts'),
          ('github', 'https://github.com/Linuturk'),
          ('facebook', 'https://www.facebook.com/linuturk'),
          ('twitter', 'https://twitter.com/linuturk'),
          ('linkedin', 'http://www.linkedin.com/in/linuturk'),)

# static paths will be copied under the same name
STATIC_PATHS = ['images',
                'slides'
                ]

# Define the location of the STATIC_PATHS above if it differs.
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/loaderio-4d9e22aa4f9e2acb7e6a99381a6937d6.txt': {'path': 'loaderio-4d9e22aa4f9e2acb7e6a99381a6937d6.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'}
        }

# Enable pages on the menu
DISPLAY_PAGES_ON_MENU = True

# Page settings
PAGE_PATHS = ['pages']
ARTICLE_EXCLUDES = (('pages',))

# External Services
GOOGLE_ANALYTICS = "UA-34793085-1"
TWITTER_USERNAME = "Linuturk"
DISQUS_SITENAME = "linuturksnatter"
