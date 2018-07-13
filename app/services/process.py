from config import Config
from os import path
from subprocess import call

def run(file_name):
    source = path.join(Config.PATHS['source'], file_name);
    resized = path.join(Config.PATHS['resized'], file_name);
    aligned = path.join(Config.PATHS['aligned'], file_name);
    black = path.join(Config.PATHS['black'], file_name);
    cropped = path.join(Config.PATHS['cropped'], file_name);

    call(f'convert -resize 1070 {source} {resized}', shell=True)
    call(f'magick {resized} -verbose -deskew 40% -trim {aligned}', shell=True)
    call(f'magick {aligned} -level 100,5000,1 -threshold 70% {black}', shell=True)
    call(f'convert -crop 980x1040+50+70 {black} {cropped}', shell=True)

    return True;
