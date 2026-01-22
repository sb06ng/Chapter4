import itertools


def infinite_fibonacci():
    """An infinite generator for the Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        # Update the state: the next number is the sum of the previous two
        a, b = b, a + b


# 1. Initialize the infinite generator
fib_gen = infinite_fibonacci()

# 2. Use islice to grab only the 1000 number
# skip all first 999 iterations
fib_iter = itertools.islice(fib_gen, 999, 1000)
target_num = next(fib_iter, "Error: couldn't fetch the 1000 number")

print(f"The 1000th Fibonacci number is: {target_num}")
