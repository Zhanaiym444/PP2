import math
import itertools
import random

def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]
