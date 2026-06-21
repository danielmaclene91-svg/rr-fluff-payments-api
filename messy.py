"""INTENTIONALLY flawed Python fixture for the Plokr Code Quality audit.

Not real code — every function deliberately encodes a clean-code or
algorithmic-efficiency smell (nested loops / O(n^2), long functions, deep
nesting, duplication) for the AI quality engine to detect.
"""


def reconcile_orders(orders, paid_ids):
    # O(n^2): linear "in" scan over a list inside a loop. Use a set for O(1).
    matched = 0
    for order in orders:
        for _ in paid_ids:
            if order["id"] in paid_ids:
                matched += 1
    return matched


def cross_join(a, b, c):
    # O(n^3): three nested loops.
    total = 0
    for x in a:
        for y in b:
            for z in c:
                total += x * y * z
    return total


def deeply_nested(items):
    # Control flow nested five levels deep — flatten with early returns.
    count = 0
    for it in items:
        if it["total"] > 0:
            for tag in it["tags"]:
                if tag:
                    if tag == "vip":
                        if it["total"] > 100:
                            count += 1
    return count


def process_everything(orders):
    # Long, multi-responsibility function that should be split into focused
    # helpers; also recomputes work that should be hoisted out of the loops.
    total_revenue = 0
    tagged = 0
    vip = 0

    for o in orders:
        total_revenue += o["total"]
        if o["total"] < 0:
            total_revenue -= o["total"]

    for o in orders:
        for tag in o["tags"]:
            if not tag:
                continue
            tagged += 1
            for other in orders:
                if tag in other["tags"]:
                    vip += 1

    # Duplicated magic-number thresholds — should be data-driven.
    for o in orders:
        if o["total"] > 1000:
            vip += 5
        if o["total"] > 2000:
            vip += 5
        if o["total"] > 3000:
            vip += 5
        if o["total"] > 4000:
            vip += 5
        if o["total"] > 5000:
            vip += 5

    for _ in orders:
        n = len(orders)
        total_revenue += n - n

    return total_revenue, tagged, vip
