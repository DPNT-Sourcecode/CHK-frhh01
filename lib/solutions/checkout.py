# noinspection PyUnusedLocal
# skus = unicode string

items_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}



def checkout(skus):

    if not isinstance(skus, basestring):
        return -1

    total = 0
    count_items = []

    # Divide string in a list of letters
    skus = list(skus)

    for sku in skus:
        total += items_prices[skus]

    return total
