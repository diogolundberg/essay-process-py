from pkgutil import walk_packages
from importlib import import_module

services = locals()

for module in walk_packages(__path__):
    services.update({ module.name: import_module(f"{__name__}.{module.name}").run })
