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
    ENV = 'production'


class Development(Config):
    ENV = 'development'
    DEBUG = True


class Testing(Config):
    ENV = 'testing'
    TESTING = True


for folder in Config.PATHS.values():
    if not path.exists(folder): makedirs(folder)
