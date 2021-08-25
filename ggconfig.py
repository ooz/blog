#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://oliz.io/blog',
        'generate_sitemap': True,
        'additional_sitemap_entries': [],
        'title': 'Oliver Z.',
        'logo': 'static/owl.png',
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
        'github': 'https://github.com/ooz',
        'about': 'https://oliz.io/about.html'
    }
}
