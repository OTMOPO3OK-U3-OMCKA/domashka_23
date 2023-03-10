import numpy


def get_unique(data, value=None):
    try:
        return list(set(data))[:int(value)]
    except ValueError:
        return list(set(data))


def get_filter(data, text=""):
    if type(text) is str:
        return list(filter(lambda x: text in x, data))
    return []


def get_sorted(data, val=True):
    try:
        if val == "desc":
            return sorted(data, reverse=True)
        return sorted(data, reverse=False)
    except IndexError:
        return sorted(data, reverse=False)


def get_map(data, value=0):
    try:
        return list(map(lambda x: x.split(" ")[int(value)], data))
    except (IndexError, ValueError):
        return []


dict_cmd = {
    "sorted": get_sorted,
    "filter": get_filter,
    "unique": get_unique,
    "map": get_map
}
