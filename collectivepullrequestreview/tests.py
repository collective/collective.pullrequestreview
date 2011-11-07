import unittest2 as unittest
from pyramid.httpexceptions import HTTPNotFound

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_pull_request_event_type(self):
        from collectivepullrequestreview.views import PullRequestView
        request = testing.DummyRequest(headers={'X-Github-Event': 'pull_request',
                                                'Content-Type': 'application/json'})
        info = PullRequestView(request)()
        self.assertEqual(info['type'], 'pull_request')

    def test_unknown_event_type(self):
        from collectivepullrequestreview.views import PullRequestView
        request = testing.DummyRequest(headers={'Content-Type': 'application/json'})
        with self.assertRaises(HTTPNotFound) as e:
            info = PullRequestView(request)()
