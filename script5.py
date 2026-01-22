def calculate_total_price(items):
    """
    Calculates the sum of discounted prices.
    Each item is a tuple: (price, discount_percentage)
    """
    # Generator expression: (price * (1 - discount/100))
    # This happens "on-the-fly" inside the sum() function
    return sum(price * (1 - discount / 100) for price, discount in items)

# --- Usage ---
# Items: ($100, 10% off), ($50, 20% off), ($200, 0% off)
shopping_cart = [(100, 10), (50, 20), (200, 0)]

total = calculate_total_price(shopping_cart)
print(f"Total Discounted Price: ${total:.2f}")