import datetime

import jwt
from bframe import current_app, request


def encode_token(payload, exps):
    return jwt.encode(payload={
        "exp": datetime.datetime.now() + datetime.timedelta(seconds=exps),
        "payload": payload,
    }, key=current_app.Config.get("SECURE_KEY"), algorithm="HS256")


def decode_token(token, verify_exp=True):
    try:
        return True, jwt.decode(token, current_app.Config.get("SECURE_KEY"),
                                algorithms=["HS256"],
                                options={"verify_exp": verify_exp})
    except jwt.ExpiredSignatureError:
        return False, "token过期"
    except Exception as e:
        return False, "异常的token"


def parse_token():
    token = request.headers.get("Authorization")
    if token is not None:
        return token[len("Bearer "):]
    return token
