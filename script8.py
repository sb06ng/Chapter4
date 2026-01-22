import itertools

def repeat_elements(data, count):
    """
    Creates a new list where each element from 'data'
    is repeated 'count' times using itertools.repeat.
    """
    # itertools.repeat(item, count) yields the item N times.
    # We use a nested generator expression to 'flatten' these into one list.
    return [
        repeated_item
        for item in data
        for repeated_item in itertools.repeat(item, count)
    ]

# --- Usage ---
my_list = ['A', 'B', 'C']
repeat_count = 3

result = repeat_elements(my_list, repeat_count)
print(f"Original: {my_list}")
print(f"Repeated: {result}")