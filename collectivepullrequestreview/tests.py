import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from collectivepullrequestreview.views import my_view
        request = testing.DummyRequest(headers={'X-Github-Event': 'pull_request',
                                                'Content-Type': 'application/json'})
        info = my_view(request)
        self.assertEqual(info['project'], 'collective.pullrequestreview')
