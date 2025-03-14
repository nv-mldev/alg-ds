from viztracer import VizTracer
import pdb

tracer = VizTracer()
tracer.start()

def add(a, b):
    pdb.set_trace()  # Start debugger here
    return a + b

a = 10
b = 20
add(a, b)

tracer.stop()
tracer.save("trace.json")

x = 5
y = x
pdb.set_trace()  # Start debugger here
x = 2
print(y)
print(y)
