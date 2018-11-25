from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import User


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def home(request):
    return {'title': "Home"}


