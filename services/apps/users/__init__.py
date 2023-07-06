from bframe import Frame


def init_app(app: Frame):
    from services.apps.users.api import v1
    app.add_route("/api/v1/users", v1.UserAPI)
