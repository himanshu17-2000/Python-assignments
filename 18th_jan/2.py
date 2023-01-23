import time
def retry(func):
    def inner(times, interval):
        for i in range(times):
            time.sleep(interval) 
            func(times , interval)
    return inner 

@retry
def func(a,b):
    
    print(f"Hello i've been called after {b} seconds")



func(3,3)

