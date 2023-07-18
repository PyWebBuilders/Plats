from bframe import Frame


def init_app(app: Frame):
    from services.apps.codes.api import v1
    app.add_route("/api/v1/codes",          v1.CodeAPI)
