from config import Config
from os import path
from subprocess import call

def run(key):
    source = path.join(Config.PATHS['source'], key);
    resized = path.join(Config.PATHS['resized'], key);
    aligned = path.join(Config.PATHS['aligned'], key);
    black = path.join(Config.PATHS['black'], key);
    cropped = path.join(Config.PATHS['cropped'], key);

    call(f'convert -resize 1070 {source} {resized}', shell=True)
    call(f'magick {resized} -verbose -deskew 40% -trim {aligned}', shell=True)
    call(f'magick {aligned} -level 100,5000,1 -threshold 70% {black}', shell=True)
    call(f'convert -crop 980x1040+50+70 {black} {cropped}', shell=True)

    return True;
