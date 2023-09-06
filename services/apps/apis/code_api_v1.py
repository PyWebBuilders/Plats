from services.apps.base import BaseAPI
from services.models.codes import Code


class CodeAPI(BaseAPI):

    class_table = Code
