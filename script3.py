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

def generate_pairs_even_only(list_a, list_b):
    """
    Yields (x, y) only if x is even.
    Optimized to skip the inner loop if x is odd.
    """
    for x in list_a:
        if x % 2 == 0:
            for y in list_b:
                yield (x, y)

# --- Usage ---
nums_a = [1, 2, 3, 4]
nums_b = [10, 11]

print("using generate_pairs_even_only")
for pair in generate_pairs_even_only(nums_a, nums_b):
    print(pair)