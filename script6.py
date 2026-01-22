from functools import reduce

def flatten_list(nested_list):
    """
    Flattens a list of arbitrary depth using reduce.
    """
    def reducer(accumulator, element):
        if isinstance(element, list):
            return accumulator + flatten_list(element)
        else:
            return accumulator + [element]

    return reduce(reducer, nested_list, [])

# --- Usage ---
complex_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flat = flatten_list(complex_list)

print(f"Original: {complex_list}")
print(f"Flattened: {flat}")