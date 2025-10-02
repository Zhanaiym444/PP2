import math
import itertools
import random

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]

