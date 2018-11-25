from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import User


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def home(request):
    return {'title': "Home"}


@view_config(route_name='list_users', renderer='../templates/users.jinja2')
def list_users(request):
    users = request.dbsession.query(User)

    return {'users': users}

