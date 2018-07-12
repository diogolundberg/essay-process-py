from config import Config
from os import path, remove

def run(key):
    source = path.join(Config.PATHS['source'], key);
    resized = path.join(Config.PATHS['resized'], key);
    aligned = path.join(Config.PATHS['aligned'], key);
    black = path.join(Config.PATHS['black'], key);
    cropped = path.join(Config.PATHS['cropped'], key);
    [remove(file) for file in [source, resized, aligned, black, cropped]]

    return True
