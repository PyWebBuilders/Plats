def ok_package(data, msg="ok", status=True):
    return {
        "data": data,
        "msg": msg,
        "status": status,
    }


def bad_package(data=None, msg="failed", status=False):
    return {
        "data": data,
        "msg": msg,
        "status": status,
    }
