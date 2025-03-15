def f(x):
    x = 1
    def g():
        x = x + 1  
        print("x =", x)
    return g

x = 3
z = f(x)
z() 