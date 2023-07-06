from bframe import abort
from services import constraints


class BaseAPI:

    def get(self, *args, **kwds):
        return abort(constraints.HTTP_METHOD_NO_IMPL.code)

    def post(self, *args, **kwds):
        return abort(constraints.HTTP_METHOD_NO_IMPL.code)

    def put(self, *args, **kwds):
        return abort(constraints.HTTP_METHOD_NO_IMPL.code)

    def delete(self, *args, **kwds):
        return abort(constraints.HTTP_METHOD_NO_IMPL.code)
