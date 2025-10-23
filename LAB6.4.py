import time
import math 

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


delayed_sqrt(25100, 2123)
