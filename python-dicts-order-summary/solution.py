def summarize_orders(orders: list) -> dict:
    """
    `orders` is a list of order dictionaries. Each has the form
      {"customer": <string>, "items": {<sku string>: <quantity int>, ...}}
    The "items" dictionary may be empty. Some orders may be for
    the same customer, and different orders may include the same
    sku.

    Return a dictionary with exactly these keys:

      "units_by_customer": dict mapping each customer to the
          total quantity across ALL of that customer's orders.
          A customer whose orders are all empty is still
          present, with 0.
      "units_by_sku": dict mapping each sku to its total
          quantity across all orders.
      "top_sku": the sku with the largest total quantity. If
          several tie, the one that is alphabetically first. If
          there are no skus at all, None.
      "customers_by_sku": dict mapping each sku to a SORTED list
          of the distinct customers who ordered it (each
          customer listed once).
      "customers_by_initial": dict mapping the UPPERCASE first
          letter of each customer to a SORTED list of the
          distinct customers with that initial. Customers with
          an empty string as their label are ignored here.

    `orders` and everything inside it must not be modified, and
    no list in the result may be shared between two keys.
    """
    units_by_customer = {}
    units_by_sku = {}
    customers_by_sku = {}
    customers_by_initial = {}

    for order in orders:
        customer = order["customer"]
        item = order["items"]
        units_by_customer.setdefault(customer, 0)

        for sku, quantity in item.items():
            units_by_customer[customer] += quantity
            units_by_sku[sku] = units_by_sku.get(sku, 0) + quantity
            customers_by_sku.setdefault(sku, set()).add(customer)

        if customer != "":
            intial = customer[0].upper()
            customers_by_initial.setdefault(intial, set()).add(customer)

    customers_by_sku = {sku: sorted(customer) for sku, customer in customers_by_sku.items()}
    customers_by_initial = {intial: sorted(customer) for intial, customer in customers_by_initial.items()}

    if units_by_sku:
        max_quantity = max(units_by_sku.values())
        top_sku = min(sku for sku, quantity in units_by_sku.items() if quantity == max_quantity)

    else:
        top_sku = None

    return {
        "units_by_customer" : units_by_customer,
        "units_by_sku" : units_by_sku,
        "top_sku" : top_sku,
        "customers_by_sku" : customers_by_sku,
        "customers_by_initial" : customers_by_initial,
    }
