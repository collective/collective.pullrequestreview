from pyramid.config import Configurator
from collectivepullrequestreview.resources import Root
from pyramid.interfaces import IRequest
from .pyflakes_validation import PyflakesValidation
from .interfaces import IPullRequestValidation


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.include('githubevent')
    config.scan('.subscriber')
    config.registry.registerSubscriptionAdapter(PyflakesValidation, [IRequest], IPullRequestValidation)
    return config.make_wsgi_app()
