from inspect import stack
def n(func):
    def func_wrapper(*args, **kwargs):
        print("@" + func.__name__+ " : " + str(func.__globals__["__name__"]) + " x ")
        return func(*args, **kwargs)
    return func_wrapper


@n
def testNotify(a, b, c):
    print(str(a), str(b), str(c))

class foo():
    @n
    def lol(self):
        testNotify(1,2,3)


bar = foo()
bar.lol()

