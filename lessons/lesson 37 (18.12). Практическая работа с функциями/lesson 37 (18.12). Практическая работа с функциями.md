AUDIT_LOG = []
ORDERS_CREATED = 0

ALLOWED_STATUS = ("new", "paid", "cancelled")


def make_create_order(prefix):
    current = 0

    def create_order(customer, *products, status="new", discounts=None, **meta):
        nonlocal current
        global ORDERS_CREATED

        if status not in ALLOWED_STATUS:
            raise ValueError("Invalid status")

        if discounts is None:
            discounts = []

        current += 1
        order_id = f"{prefix}{current}"

        order = {
            "id": order_id,
            "customer": customer,
            "products": list(products),
            "discounts": list(discounts),
            "status": status,
            "meta": meta,
        }

        ORDERS_CREATED += 1
        AUDIT_LOG.append(f"create {order_id}")
        return order

    return create_order


create_order = make_create_order("ORD-")


def print_order(order, prices, tax=0.0, title=None):
    if title is None:
        title = "Заказ"

    subtotal = sum(prices.get(p, 0) for p in order["products"]) - sum(order["discounts"])
    total_value = round(subtotal * (1 + tax), 2)
    print(f"{title} {order['id']} для {order['customer']}: {total_value}")


def delivery_fee(weight_kg, cache={}, *, safe=False, safe_cache=None):
    if safe:
        if safe_cache is None:
            safe_cache = {}
        storage = safe_cache
    else:
        storage = cache

    if weight_kg in storage:
        return storage[weight_kg]
    storage[weight_kg] = round(weight_kg * 49.9, 2)
    return storage[weight_kg]


def summarize_orders(orders, prices, tax=0.0):
    totals = []
    for o in orders:
        if o["status"] == "cancelled":
            continue
        subtotal = sum(prices.get(p, 0) for p in o["products"]) - sum(o["discounts"])
        totals.append(round(subtotal * (1 + tax), 2))

    if not totals:
        return {"min": 0.0, "max": 0.0, "sum": 0.0, "avg": 0.0}

    return {
        "min": min(totals),
        "max": max(totals),
        "sum": sum(totals),
        "avg": round(sum(totals) / len(totals), 2),
    }


prices = {"coffee": 120, "croissant": 80, "tea": 70}

product_list = ["coffee", "croissant"]
order_meta = {"table": 7, "waiter": "Ann"}

o1 = create_order("Igor", *product_list, status="paid", **order_meta)
o1["products"].append("tea")
AUDIT_LOG.append(f"add_product {o1['id']}")

o2 = create_order(customer="Olga", status="new", vip=True)

delivery1 = delivery_fee(2)
delivery2 = delivery_fee(3)
delivery3 = delivery_fee(2)

delivery_cache = {}
delivery_ok_1 = delivery_fee(2, safe=True, safe_cache=delivery_cache)
delivery_ok_2 = delivery_fee(3, safe=True, safe_cache=delivery_cache)
delivery_ok_3 = delivery_fee(2, safe=True, safe_cache=delivery_cache)

print_order(o1, prices, tax=0.1)
print(summarize_orders([o1, o2], prices, tax=0.1))
print(ORDERS_CREATED)
print(delivery1, delivery2, delivery3)
print(delivery_ok_1, delivery_ok_2, delivery_ok_3)
print(AUDIT_LOG)