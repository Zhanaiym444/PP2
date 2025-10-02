import math
import itertools
import random

def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for n in nums:
        if n == code[idx]:
            idx += 1
            if idx == len(code):
                return True
    return False
