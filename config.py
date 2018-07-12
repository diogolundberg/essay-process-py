from os import getenv, path, getcwd, makedirs


class Config(object):
    BUCKET_NAME = getenv('BUCKET_NAME')
    PATHS = {
        'source': path.join(getcwd(), 'tmp/source'),
        'resized': path.join(getcwd(), 'tmp/resized'),
        'aligned': path.join(getcwd(), 'tmp/aligned'),
        'black': path.join(getcwd(), 'tmp/black'),
        'cropped': path.join(getcwd(), 'tmp/cropped'),
    }


class Production(Config):
    pass


class Development(Config):
    pass


class Testing(Config):
    pass


for folder in Config.PATHS.values():
    if not path.exists(folder): makedirs(folder)
