from app.services import download, process, upload, delete
from logger import logger
from flask import Blueprint, request

blueprint = Blueprint('messages', __name__, url_prefix='/messages')

@blueprint.route('', methods=['post'])
def index():
    records = request.json.get('Records')
    if not records: return 'ok', 200
    for record in records:
        logger.info(record)
        key = record['s3']['object']['key']
        file_name = download(key)
        process(file_name)
        upload(file_name)
    return 'ok', 200
