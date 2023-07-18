from bframe import Frame, g
from services.models import Session
from services.models.users import User
from services.utils import static
from services.utils.jwt_helper import decode_token, parse_token


def check_user_status():
    token = parse_token()
    # no token
    if not token:
        g.user = User(id=0, role=static.role_visitor())
        return

    status, payload = decode_token(token)

    # token error
    if not status:
        g.user = User(id=0, role=static.role_visitor())
        return

    payload_data = payload.get("payload")
    userid = payload_data.get("id")

    user = Session().query(User).filter(User.id == userid).first()

    # user is not exists
    if not user:
        g.user = User(id=0, role=static.role_visitor())
        return

    g.user = user


def init_app(app: Frame):
    app.add_before_handle(check_user_status)
