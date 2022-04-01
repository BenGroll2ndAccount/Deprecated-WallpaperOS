import time
from notifier import NotifyService




def log(func):
    def func_wrapper(*args, **kwargs):
        if NotifyService.get("debug.widget-log_any_function_call"):
            print("@" + func.__name__+ " : " + str(func.__globals__["__name__"]) + " x " + str(time.time()))
        return func(*args, **kwargs)
    return func_wrapper

