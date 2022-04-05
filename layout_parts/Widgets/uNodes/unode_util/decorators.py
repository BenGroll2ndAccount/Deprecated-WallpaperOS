import time
from notifier import NotifyService
def log(func):
    def func_wrapper(*args, **kwargs):
        if NotifyService.get("debug.widget-log_any_function_call"):
            print("@" + func.__name__+ " : " + str(func.__globals__["__name__"]) + " x ")
        return func(*args, **kwargs)
    return func_wrapper

def tlog(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        taken_s = (end-start)
        suffix = "(" + str(round(float(taken_s * 1000), 2)) + "ms)"
        if NotifyService.get("debug.widget-log_any_function_call"):
            print("@" + str(func.__globals__["__name__"])+ " : " +  func.__name__ + suffix)
        return result
    return timed



