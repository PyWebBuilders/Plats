def init_app(app):
    from services.apps.users import init_app
    init_app(app)