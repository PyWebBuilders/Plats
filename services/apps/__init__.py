def init_app(app):
    from services.apps.users import init_app as init_user
    init_user(app)
    from services.apps.codes import init_app as init_code
    init_code(app)