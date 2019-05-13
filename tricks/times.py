import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('{} cost {}'.format(func.__name__ ,end_time - start_time))
        return result
    return wrapper


@timeit
def test(t):
    time.sleep(t)
    return 2 * t

print(test(3))
