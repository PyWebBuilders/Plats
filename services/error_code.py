import functools

from bframe import Frame
from bframe.wrappers import Response

from services import constraints


def error_100000(desc=""):
    return Response(200, body=desc)


def init_error_handle(app: Frame):
    for attr in constraints.__dict__:
        if attr.startswith("HTTP_"):
            attr_o = getattr(constraints, attr)
            callable_name = "error_%s" % attr_o.code
            target = globals().get(callable_name)
            if target and callable(target):
                app.error_funs_dict[attr_o.code] = functools.partial(target,
                                                                     attr_o.code_msg)
