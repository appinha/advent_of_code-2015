def is_int(object):
    return (isinstance(object, int))

def is_str(object):
    return (isinstance(object, str))

def is_list(object):
    return (isinstance(object, list))

def is_dict(object):
    return (isinstance(object, dict))

def str_to_int(object):
    if object.isdigit():
        return int(object)
    else:
        return object
