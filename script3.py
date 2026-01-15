import itertools


def generate_pairs(list_a, list_b):
    """Yields the Cartesian Product of two lists."""
    for x in list_a:
        for y in list_b:
            yield (x, y)


# --- Usage ---
colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]

pairs = generate_pairs(colors, sizes)

print("using generate_pairs")
for pair in pairs:
    print(pair)

# This does exactly what our generator function does, but in C
pairs = itertools.product(colors, sizes)
print("using itertools.product")
for pair in pairs:
    print(pair)
