import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@log_execution_time
def slow_function():
    time.sleep(2)
    print("Finished slow function!")

@log_execution_time
def fast_function():
    time.sleep(0.5)
    print("Finished fast function!")

@log_execution_time
def sum_numbers(a, b):
    time.sleep(1)
    return a + b

slow_function()
fast_function()
result = sum_numbers(10, 20)
print(f"Sum result: {result}")
