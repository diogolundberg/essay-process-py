import config
from os import getenv
from sanic import Sanic
from .controllers import controllers

application = Sanic()
application.config.from_object(getattr(config, getenv('ENV', 'Development')))
application.blueprint(controllers)
