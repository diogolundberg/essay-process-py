from app.services import download, process, upload, delete
from flask import Blueprint, request

blueprint = Blueprint('messages', __name__, url_prefix='/messages')

@blueprint.route('', methods=['post'])
def index():
    records = request.json.get('Records')
    if not records: return 'ok', 200
    for record in records:
        key = record['s3']['object']['key']
        download(key)
        process(key)
        upload(key)
    return 'ok', 200
