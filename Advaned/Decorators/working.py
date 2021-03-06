import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print("fine",func(*args,**kwargs))
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,5)
out_square = calc_square(array)
print("out_square",out_square)

out_cube = calc_cube(array)
print("calc_cube",calc_cube)
