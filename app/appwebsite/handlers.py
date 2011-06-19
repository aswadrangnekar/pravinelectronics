# -*- coding: utf-8 -*-
"""
    hello_world.handlers
    ~~~~~~~~~~~~~~~~~~~~

    Hello, World!: the simplest tipfy app.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE for more details.
"""
from tipfy.app import Response
from tipfy.handler import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin

class LandingPageHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        """Simply returns a rendered template with an enigmatic salutation."""
        context = {
            'message': 'Pravin Electronics - Work in progress, stay tuned!',
        }
        return self.render_response('landing_page.html', **context)
