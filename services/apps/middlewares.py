from bframe import Frame, g
from services.models import Session
from services.models.users import User
from services.utils.jwt_helper import decode_token, parse_token


def check_user_status():
    token = parse_token()
    # no token
    if not token:
        g.user = None
        return

    status, payload = decode_token(token)

    # token error
    if not status:
        g.user = None
        return

    payload_data = payload.get("payload")
    userid = payload_data.get("id")

    user = Session().query(User).filter(User.id == userid).first()

    # user is not exists
    if not user:
        g.user = None
        return

    g.user = user


def init_app(app: Frame):
    app.add_before_handle(check_user_status)
