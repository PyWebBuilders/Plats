from bframe import current_app, request
from services.apps.base import BaseAPI
from services.models import Session
from services.models.users import User
from services.utils import static
from services.utils.jwt_helper import encode_token, parse_token, decode_token
from services.utils.orm import object_2_dict, objects_2_dict
from services.utils.package import bad_package, ok_package


def register():
    """注册账号"""
    username = request.forms.get("username")
    password = request.forms.get("password")

    if not all([username, password]):
        return bad_package("参数缺失")

    users = Session().query(User).filter(User.username == username).all()
    if len(users):
        return bad_package("账号已被注册")

    try:
        user = User(username=username,
                    password=password,
                    role=static.role_user())
        Session.add(user)
        Session.commit()
    except Exception as e:
        Session.rollback()
        return bad_package("账户注册异常")

    token = encode_token(payload={
        "id": user.id
    }, exps=current_app.Config.get("TOEKN_EXPIRE"))

    json_data = object_2_dict(user)
    json_data["token"] = token
    return ok_package(json_data)


def refresh_token():
    """刷新token"""
    token = parse_token()
    status, payload = decode_token(token)
    if not status:
        return bad_package("失效的token")
    return ok_package(encode_token(payload.get("payload"),
                                   exps=current_app.Config.get("TOEKN_EXPIRE")))


class UserAPI(BaseAPI):

    def get(self, *args, **kwds):
        users = Session().query(User).all()
        return ok_package(objects_2_dict(users))
