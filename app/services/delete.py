from config import Config
from os import path, remove

def run(file_name):
    source = path.join(Config.PATHS['source'], file_name);
    resized = path.join(Config.PATHS['resized'], file_name);
    aligned = path.join(Config.PATHS['aligned'], file_name);
    black = path.join(Config.PATHS['black'], file_name);
    cropped = path.join(Config.PATHS['cropped'], file_name);

    map(remove, [source, resized, aligned, black, cropped])

    return True
