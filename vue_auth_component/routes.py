def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('register', '/register')
    config.add_route('list_users', '/users')

    config.add_route('verify_username_and_email', '/verify_username_and_email')
