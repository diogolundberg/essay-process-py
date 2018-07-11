from pkgutil import walk_packages
from importlib import import_module
from sanic.blueprints import Blueprint

modules = [import_module(f"{__name__}.{module.name}").blueprint
           for module in walk_packages(__path__)]

controllers = Blueprint.group(*modules, url_prefix='/')
