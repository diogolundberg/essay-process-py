from app.services import download, process, upload, delete
from flask import Blueprint, request

blueprint = Blueprint('messages', __name__, url_prefix='/messages')

@blueprint.route('', methods=['post'])
def index():
    key = request.json['Records'][0]['s3']['object']['key']
    download(key)
    process(key)
    upload(key)
    return key
