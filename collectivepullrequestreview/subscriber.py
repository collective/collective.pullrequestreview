# -*- coding: utf-8 -*-
"""
collective.pullrequestreview

Licensed under the GPL license, see LICENCE.txt for more details.
"""

from pyramid.events import subscriber
from pyramid.view import render_view
from githubevent.events import PullRequest
from .gitclone import GitClone
from .interfaces import IPullRequestValidation


@subscriber(PullRequest)
class PullRequestSubscriber(object):

    def __init__(self, request):
        self.request = request

    @property
    def validators(self):
        registry = self.request.registry
        for validator in registry.subscribers((self.request,), IPullRequestValidation):
            yield validator

    def validate(self, repository):
        validationResults = []
        for validator in self.validators:
            validationResults.append(validator.validate(repository))
        return validationResults

    def __call__(self):
        with GitClone(self.request.base_repo_name, self.request.base_repo_url) as repo:
            validationResults = self.validate(repo)
            repo.merge(self.request.head_repo_url)
            validationResutlsAfter = self.validate(repo)
            validationView = render_view((validationResults, validationResutlsAfter),
                    self.request, 'view')
            # ADD VIEW.render TO COMMENT
