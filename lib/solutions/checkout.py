# noinspection PyUnusedLocal
# skus = unicode string

items_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}
items_rules = {
    'A': {
        'items': 3,
        'sub': 20
    },
    'B': {
        'items': 2,
        'sub': 15
    }
}



def checkout(skus):

    if not isinstance(skus, str):
        return -1

    total = 0
    count_items = []

    # Divide string in a list of letters
    skus = list(skus)

    for sku in skus:
        # Check if it is a valid item
        if sku in items_prices:

            count_items.append(sku)

            if sku in items_rules:
                if count_items.count(sku) % items_rules[sku]['items'] == 0:
                    price = items_prices[sku] - items_rules[sku]['sub']
                else:
                    price = items_prices[sku]
            else:
                price = items_prices[sku]

            print(price)
            total += price

    return total