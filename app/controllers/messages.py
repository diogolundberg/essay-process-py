from sanic.response import json, text
from sanic import Blueprint
from app.services import download

blueprint = Blueprint('messages', url_prefix='/messages')

@blueprint.post('/')
async def index(request):
    file = download(request.json['Records'][0]['s3']['object']['key'])
    results = process(file)
    upload(results)
    return text(file)
