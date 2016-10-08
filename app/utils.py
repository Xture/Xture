import collections


def objectid_fix(elem):
    if elem is None:
        return elem
    if isinstance(elem, collections.Iterable):
        for elem_ in elem:
            objectid_fix(elem_)
        return elem
    else:
        elem['_id'] = str(elem['_id'])
        return elem
