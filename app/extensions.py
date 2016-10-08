import collections


def objectid_stringify(list_):
    if isinstance(list_, collections.Iterable):
        for elem in list_:
            elem['_id'] = str(elem['_id'])
        return list_
    else:
        list_['_id'] = str(list_['_id'])
        return list_
