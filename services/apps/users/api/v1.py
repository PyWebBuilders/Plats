from services.apps.base import BaseAPI
from services.models import Session
from services.models.users import User
from services.utils.orm import objects_2_dict
from services.utils.package import ok_package


class UserAPI(BaseAPI):
    
    def get(self, *args, **kwds):
        users = Session().query(User).all()
        return ok_package(objects_2_dict(users))
