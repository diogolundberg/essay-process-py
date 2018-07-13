from os import getenv
from flask import Flask
from .controllers import blueprints

application = Flask('educat')
application.config.from_object(f'config.{getenv("ENV", "Development")}')

for blueprint in blueprints: application.register_blueprint(blueprint)
