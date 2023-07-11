from bframe import Frame


def init_app(app: Frame):
    from services.apps.users.api import v1
    app.add_route("/api/v1/register", v1.register, ["POST"])
    app.add_route("/api/v1/refresh_token", v1.refresh_token)
    app.add_route("/api/v1/users", v1.UserAPI)
