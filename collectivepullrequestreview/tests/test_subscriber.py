# -*- coding: utf-8 -*-
"""
collective.pullrequestreview

Licensed under the GPL license, see LICENCE.txt for more details.
"""
import pkg_resources
import unittest
from pyramid import testing
from ..subscriber import PullRequestSubscriber
from githubevent.testing import DummyGitHubPullRequest

EXAMPLE = pkg_resources.resource_string('collectivepullrequestreview', 'examples/pullrequest.dump')


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def testBasicRequest(self):
        request = DummyGitHubPullRequest()
        request.body = EXAMPLE
        from pyramid.interfaces import IRequest
        from ..pyflakes_validation import PyflakesValidation
        from ..interfaces import IPullRequestValidation
        self.config.registry.registerSubscriptionAdapter(PyflakesValidation, [IRequest], IPullRequestValidation)
        self.assertEqual(request.base_repo_url,
                'git://github.com/vincentfretin/collective.pullrequestreview.git')
        self.assertEqual(request.head_repo_url,
                'git://github.com/collective/collective.pullrequestreview.git')
        view = PullRequestSubscriber(request)
        view()
