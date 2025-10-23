from functools import reduce
import math

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply_list([2, 3, 4, 5]))