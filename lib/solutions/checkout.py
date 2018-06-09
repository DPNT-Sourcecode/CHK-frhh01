# noinspection PyUnusedLocal
# skus = unicode string

items_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
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
    ],
    'H': [
        {
            'items': 5,
            'sub': 5
        },
        {
            'items': 10,
            'sub': 20
        }
    ],
    'K': [
        {
            'items': 2,
            'sub': 10
        }
    ],
    'P': [
        {
            'items': 5,
            'sub': 50
        }
    ],
    'Q': [
        {
            'items': 3,
            'sub': 10
        }
    ],
    'V': [
        {
            'items': 3,
            'sub': 20
        },
        {
            'items': 2,
            'sub': 10
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
    ],
    'F': [
        {
            'quantity': 3,
            'action': 'free',
            'item': 'F',
            'n_free_items': 1
        }
    ],
    'N': [
        {
            'quantity': 3,
            'action': 'free',
            'item': 'M',
            'n_free_items': 1
        }
    ],
    'R': [
        {
            'quantity': 3,
            'action': 'free',
            'item': 'Q',
            'n_free_items': 1
        }
    ],
    'U': [
        {
            'quantity': 3,
            'action': 'free',
            'item': 'U',
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
                    if options[0]['item'] in items_count:
                        n_free_items = int(items_count[item_free] / options[0]['quantity'])

                        # Remove items
                        items_count[options[0]['item']] -= n_free_items
                        if items_count[options[0]['item']] < 0:
                            items_count[options[0]['item']] = 0

    # Recreate skus
    skus = ""
    for item, count in items_count.iteritems():
        for i in range(0, count):
            skus += item


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
                            count -= rule["items"]
                            items_count[item] -= rule["items"]
                            discountMatch = True
                            break

        if not discountMatch:
            break

    # Calculate total
    for sku in skus:
        total += items_prices[sku]
    total -= discount

    return total

print(checkout("HHHHHHHHHH"))