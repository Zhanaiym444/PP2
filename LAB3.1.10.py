import math
import itertools
import random

def unique_list(lst):
    uniq = []
    for x in lst:
        if x not in uniq:
            uniq.append(x)
    return uniq
