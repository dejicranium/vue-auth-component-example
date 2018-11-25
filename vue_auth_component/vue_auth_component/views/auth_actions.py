from pyramid.view import view_config
from ..models import User


@view_config(route_name='verify_username_and_email', renderer='json')
def verify_username_and_email(request):
    error_exists = False
    error_text = ''

    # 'i' here stands for initial
    i_email = request.json_body.get('email', None)
    i_username = request.json_body.get('username', None)

    email = request.dbsession.query(User).filter_by(email=i_email)
    if email.scalar():
        error_exists = True
        error_text = 'Email already exists'

    username = request.dbsession.query(User).filter_by(username=i_username)
    if username.scalar():
        error_exists = True
        if error_text:
            error_text = "Email and username already exist"
        else:
            error_text = "Username already exists"

    
    # at this point, it is obvious that we can't continue with registration.
        
    if error_exists:
        return {'status': 'error', 'errorText': error_text}

    request.response.status = '200'
    return {'status': 'success'}


@view_config(route_name='register', renderer='json')
def register(request):
    body = request.json_body
    first_name = body.get('firstName', None)
    last_name = body.get('lastName', None)
    email = body.get('email', None)
    username = body.get('username', None)
    password = body.get('password', None)

    new_user = User()

    try:
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.email = email
        new_user.username = username

        request.dbsession.add(new_user)

    except Exception as e:
        return {"status": e}

    

    

    