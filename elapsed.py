import time
def elapsedtime(start):
    end = time.time()
    taken_s = (end-start)
    suffix = "(" + str(round(float(taken_s * 1000), 2)) + "ms)"
    print(suffix)
