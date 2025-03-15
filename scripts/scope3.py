def make_counter():
    count = 0

    def inner():
        nonlocal count  # Modify the 'count' from make_counter's scope
        count += 1
        return count

    return inner

counter1 = make_counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2

counter2 = make_counter()
print(counter2())  # Output: 1
print(counter1()) # Output: 3