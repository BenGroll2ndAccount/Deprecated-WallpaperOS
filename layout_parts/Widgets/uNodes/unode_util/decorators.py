import time
from notifier import NotifyService
from inspect import stack

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
        suffix = "(" + str(round(float(taken_s * 1000), 5)) + "ms)"       
        if NotifyService.get("debug.widget-log_any_function_call"):
                print("@" + str(func.__globals__["__name__"])+ " : " +  func.__name__ + suffix)
        return result
    return timed

def n(func):
    def func_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        caller = stack()[1].function
        print(func.__name__)
        if NotifyService.get("debug.widget-log_notifications") : print("@" + str(func.__globals__["__name__"]) + " : " + func.__name__ + "(*args = " + str(args) + ", **kwargs = " + str(kwargs) + ")\n")
        return result
    return func_wrapper


