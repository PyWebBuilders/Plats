from bframe import g
import functools
from services.utils.package import bad_package


def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        if g.user is None:
            return bad_package("login_required")
        return f(*args, **kwds)
    return wrapper
