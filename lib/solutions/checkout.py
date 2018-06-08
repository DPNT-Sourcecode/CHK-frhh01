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

    items_count = {}

    total = 0
    # Divide string in a list of letters
    skus = list(skus)

    for sku in skus:

        # Check if it is a valid item
        if sku in items_prices:

            if sku not in items_count:
                items_count[sku] = 0

            items_count[sku] += 1

        else:
            return -1

    # Remove items if there are some discounts
    for item, count in items_count.iteritems():
        for item_free, options in items_free.iteritems():
            if item_free == item:
                if options[0]["action"] == "free":

                    # Define how many items are for free
                    n_free_items = int(items_count[options[0]['item']] / options[0]['quantity'])

                    # Remove items
                    items_count[options[0]['item']] -= n_free_items
                    if items_count[options[0]['item']] < 0:
                        items_count[options[0]['item']] = 0

    # Recreate skus
    skus = ""
    for item, count in items_count.iteritems():
        for i in range(0, count):
            skus += item
    print(skus)

    # Do discounts
    discount = 0

    while True:
        discountMatch = False
        for item, rules in items_rules.iteritems():
            for item_count, count in items_count.iteritems():
                if item == item_count:
                    for rule in rules:
                        if count >= rule["items"]:
                            discount += rule["sub"]
                            # Remove discounted items
                            items_count[item] -= rule["items"]
                            discountMatch = True

        if not discountMatch:
            break

    # Calculate total
    for sku in skus:
        total += items_prices[sku]
    total -= discount

    return total
