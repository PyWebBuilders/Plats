def init_app(app):
    from services.apps.apis import user_api_v1
    app.add_route("/api/v1/register",       user_api_v1.register,        ["POST"])  # noqa
    app.add_route("/api/v1/login",          user_api_v1.login,           ["POST"])  # noqa
    app.add_route("/api/v1/refresh_token",  user_api_v1.refresh_token)
    app.add_route("/api/v1/users",          user_api_v1.UserAPI)

    from services.apps.apis import code_api_v1
    app.add_route("/api/v1/codes",          code_api_v1.CodeAPI)
