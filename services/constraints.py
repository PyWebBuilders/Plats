from collections import namedtuple

__error_code = namedtuple("__error_code", ["code", "code_msg", "log_msg"])

HTTP_METHOD_NO_IMPL = __error_code(100000, "website building", "方法未实现")
