#from timeit import Timer
from threading import Timer

def hello():
    print("hello, timer")

t = Timer(5.0, hello)
t.start() 
