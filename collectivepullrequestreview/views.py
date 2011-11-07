from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound


@view_config(renderer="string")
class PullRequestView(object):
    def __init__(self, request):
        self.request = request

    def __call__(self):
        event_type = self.request.headers.get('X-Github-Event')
        if event_type == 'pull_request':
            return {'type': event_type}
        raise HTTPNotFound()
