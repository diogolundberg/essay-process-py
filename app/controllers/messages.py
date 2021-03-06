from app.services import download, process, upload, delete
from flask import Blueprint, request
import logging
import logging.handlers
import re


from os import getcwd, path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

LOG_FILE = path.join(getcwd(), 'requests.log')
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

blueprint = Blueprint('messages', __name__, url_prefix='/messages')

@blueprint.route('', methods=['post'])
def index():
    records = request.json.get('Records')
    if not records: return 'ok', 200
    for record in records:
        logger.info(record)
        key = record['s3']['object']['key']
        file_name = re.sub(r'^[^/]+/', '', key)
        download(key, file_name)
        process(file_name)
        upload(file_name)
    return 'ok', 200
