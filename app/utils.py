import collections


def objectid_fix(elem):
    if isinstance(elem, collections.Iterable):
        for elem_ in elem:
            elem_['_id'] = str(elem_['_id'])
        return elem
    else:
        elem['_id'] = str(elem['_id'])
        return elem
