# -*- coding: utf-8 -*-
from zope.interface import implements
from .interfaces import IPullRequestValidation


class PullRequestValidation(object):
    implements(IPullRequestValidation)

    def __init__(self, request):
        self.request = request
