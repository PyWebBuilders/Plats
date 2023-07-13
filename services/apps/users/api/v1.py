from bframe import current_app, g, request
from services.apps.base import BaseAPI
from services.apps.decorators import login_required
from services.models import Session
from services.models.users import User
from services.utils import static
from services.utils.jwt_helper import decode_token, encode_token, parse_token
from services.utils.orm import object_2_dict, objects_2_dict
from services.utils.package import bad_package, ok_package
from services.utils.role_helper import check_role
from sqlalchemy import or_


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


def login():
    """账号登录"""
    username = request.forms.get("username")
    password = request.forms.get("password")

    if not all([username, password]):
        return bad_package("参数缺失")

    user = Session().query(User).filter(or_(
        User.username == username,
        User.email == username,
    )).first()
    if user is None:
        return bad_package("账号或密码错误")

    if user.password != password:
        return bad_package("账号或密码错误")

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

    @login_required
    def get(self, *args, **kwds):
        query = Session().query(User)
        if check_role() != static.role_admin():
            query = query.filter(User.id==g.user.id)
        users = query.all()
        return ok_package(objects_2_dict(users))
