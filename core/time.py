import time

def now():
    return time.time()

def dt(last_t: float) -> float:
    return now() - last_t