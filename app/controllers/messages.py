from app.services import download, process, upload, delete
from sanic import Blueprint
from sanic.response import json, text

blueprint = Blueprint('messages', url_prefix='/messages')

@blueprint.post('/')
async def index(request):
    key = request.json['Records'][0]['s3']['object']['key']
    download(key)
    process(key)
    upload(key)
    delete(key)
    return text(key)
