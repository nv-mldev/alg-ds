
# Static Scoping (Python)
x = 10

def outer():
    x = 20
    def inner():
        print("Inside Inner (Python):", x) #static lookup
    inner()
    standalone()

def standalone():
    print("Inside Standalone (Python):", x) #static lookup

outer()
standalone()