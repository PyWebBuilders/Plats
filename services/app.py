from bframe import Frame
from bframe.server import HTTP_METHOD


def create_app(config):
    app = Frame(__name__)
    app.Config.from_py(config)

    @app.route("/api/ping", method=HTTP_METHOD)
    def ping():
        from services.utils.package import ok_package
        if app.Config["DEBUG"]:
            from bframe import request
            return ok_package("pong %s" % request.method)
        return ok_package("pong")

    from services.models import init_app as init_models
    init_models(app)

    from services.error_code import init_error_handle
    init_error_handle(app)

    from services.apps import init_app as init_apps
    init_apps(app)

    return app
