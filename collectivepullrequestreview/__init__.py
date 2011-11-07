from pyramid.config import Configurator
from collectivepullrequestreview.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_static_view('static', 'collectivepullrequestreview:static')
    config.scan()
    return config.make_wsgi_app()

