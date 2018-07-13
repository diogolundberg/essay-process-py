from pkgutil import walk_packages
from importlib import import_module

blueprints = [import_module(f"{__name__}.{module.name}").blueprint
           for module in walk_packages(__path__)]
