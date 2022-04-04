#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://oliz.io/blog',
        'generate_sitemap': True,
        'generate_rss': True,
        'additional_sitemap_entries': [],
        'title': 'Oli Z.',
        'logo': 'static/owl_256.png',
        'head': [
            '''<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">''',
            '''<meta name="referrer" content="no-referrer">'''
        ]
    },
    'author': {
        'name': 'oz',
        'url': 'https://oliz.io'
    },
    'social': {
        'blog': 'https://oliz.io/blog/',
        'rss': 'https://oliz.io/blog/rss.xml',
        'links': 'https://oliz.io/links.html',
        'about': 'https://oliz.io/about.html'
    }
}
