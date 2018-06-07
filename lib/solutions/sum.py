# noinspection PyShadowingBuiltins,PyUnusedLocal
def sum(x, y):
    # Check if x and y are integer between 0 and 100
    if not isinstance(x, int) or not isinstance(y, int):
        return None
    if x >= 0 and x <= 100 and y >= 0 and y <= 100:
        return x + y
    return None
    # raise NotImplementedError()
