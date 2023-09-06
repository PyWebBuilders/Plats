from bframe import MethodView, abort, g
from services import constraints
from services.apps.decorators import class_login_required
from services.models import Session
from services.utils import static
from services.utils.orm import objects_2_dict
from services.utils.package import bad_package, ok_package
from services.utils.role_helper import check_role


@class_login_required
class BaseAPI(MethodView):

    class_table = None

    def get(self, *args, **kwds):
        query = Session().query(self.class_table).\
            filter(self.class_table.state == static.state_valid())
        if check_role() != static.role_admin():
            query = query.filter(self.class_table.id == g.user.id)
        objs = query.all()
        return ok_package(objects_2_dict(objs))

    def post(self, *args, **kwds):
        return abort(constraints.HTTP_METHOD_NO_IMPL.code)

    def put(self, *args, **kwds):
        return abort(constraints.HTTP_METHOD_NO_IMPL.code)

    def delete(self, *args, **kwds):
        return abort(constraints.HTTP_METHOD_NO_IMPL.code)
