def calculate_total(items):
    """
    Calculate total price of items.
    """
    return sum(item["price"] for item in items)


def apply_discount(total, discount_percent):
    """
    Apply percentage discount to total amount.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount percentage")

    discount = (discount_percent / 100) * total
    return total - discount


def print_invoice(items, discount_percent=0):
    """
    Print invoice with total and discount applied.
    """
    total = calculate_total(items)
    final_amount = apply_discount(total, discount_percent)

    print("------ Invoice ------")
    print(f"Total: {total}")
    print(f"Discount: {discount_percent}%")
    print(f"Final Amount: {final_amount}")
    print("---------------------")


if __name__ == "__main__":
    items = [
        {"name": "Book", "price": 200},
        {"name": "Pen", "price": 50},
    ]

    print_invoice(items, discount_percent=10)