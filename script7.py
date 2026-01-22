import string


def unique_chars_generator(input_string):
    """
    Yields (char, position) for the first occurrence of
    alphanumeric characters, ignoring spaces and punctuation.
    """
    seen = set()
    for index, character in enumerate(input_string):
        if character.isalnum():
            if character not in seen:
                yield character, index
                seen.add(character)


# --- Usage ---
text = "Hello, World! 123..."
for char, pos in unique_chars_generator(text):
    print(f"Char: '{char}' at Index: {pos}")