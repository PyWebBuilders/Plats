import functools

from bframe import g
from bframe.server import HTTP_METHOD
from services.utils.package import bad_package


def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        if g.user.id == 0:
            return bad_package("login_required")
        return f(*args, **kwds)
    return wrapper


def class_login_required(cls):
    meth = [method.lower() for method in HTTP_METHOD if hasattr(cls,
                                                                method.lower())]
    for m in meth:
        m_obj = getattr(cls, m)
        setattr(cls, m, login_required(m_obj))
    return cls
