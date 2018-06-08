# noinspection PyUnusedLocal
# skus = unicode string

items_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}
items_rules = {
    'A': [
        {
            'items': 5,
            'sub': 50
        },
        {
            'items': 3,
            'sub': 20
        }
    ],
    'B': [
        {
            'items': 2,
            'sub': 15
        }
    ]
}

items_free = {
    'E': [
        {
            'quantity': 2,
            'action': 'free',
            'item': 'B',
            'n_free_items': 1
        }
    ]
}



def checkout(skus):

    count_items = []

    total = 0
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

            total += price
        else:
            return -1

    return total

