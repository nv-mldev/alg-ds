def f():
    i = 0
    def g():
        nonlocal i
        i += 1
        return i
    return g

x = f()
print(x()) # Output: 0
print(x()) # Output: 1
print(x()) # Output: 2
print(x()) # Output: 3

