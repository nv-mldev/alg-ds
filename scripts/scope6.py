def f(x):
    def g():
        x = 'abc'
        print('x =', x)

g()