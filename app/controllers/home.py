from sanic.response import text
from sanic import Blueprint

blueprint = Blueprint('home', url_prefix='/')

@blueprint.route('/')
async def index(request):
    return text('ready')
