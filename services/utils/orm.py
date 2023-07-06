def object_2_dict(obj):
    return {key.name: getattr(obj, key.name) for key in obj.__table__.columns}


def objects_2_dict(objs):
    return [object_2_dict(obj) for obj in objs]
