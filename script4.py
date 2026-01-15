def are_all_palindromes(word_list):
    # [word == word[::-1]] checks if the word equals its reverse
    return all(word == word[::-1] for word in word_list)

words_1 = ["radar", "level", "kayak"]
words_2 = ["radar", "python", "kayak"]

print(f"List 1: {are_all_palindromes(words_1)}")
print(f"List 2: {are_all_palindromes(words_2)}")