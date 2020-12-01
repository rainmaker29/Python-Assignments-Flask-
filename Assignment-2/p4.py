import time
from functools import wraps

def mytimer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("Time =  {} seconds".format(end - start))
        return result

    return wrapper

def mylogger(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        with open("logged.txt","w") as file:
            file.write(str(f(*args, **kwargs)))
        print("Logged successfully")

    return wrapper


@mylogger
@mytimer
def f(a):
    return a+2;

f(2)
