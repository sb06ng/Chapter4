class ReverseIterator:
    def __init__(self, data):
        # We store the list and start our index at the very end
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        # The 'Handshake': An iterator must return itself
        return self

    def __next__(self):
        # The 'Step': Check if we've reached the beginning of the list
        if self.index < 0:
            raise StopIteration  # The signal to stop the loop

        # Get the item, move the pointer back, and return the item
        result = self.data[self.index]
        self.index -= 1
        return result


# --- Usage ---
my_list = [10, 20, 30, 40]
rev = ReverseIterator(my_list)

for item in rev:
    print(item)

class ReverseEvenIterator:
    def __init__(self, data):
        # We store the list and start our index at the very end
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        # The 'Handshake': An iterator must return itself
        return self

    def __next__(self):
        # The 'Step': Check if we've reached the beginning of the list
        while self.index >= 0:
            result = self.data[self.index]
            self.index -= 1
            if result % 2 == 0:
                return result
        # Once the loop finishes (index < 0), stop
        raise StopIteration


# --- Usage ---
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
rev = ReverseEvenIterator(my_list)

for item in rev:
    print(item)
