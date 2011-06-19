# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    Rule('/', name='LandingPage', handler='appwebsite.handlers.LandingPageHandler'),
]
