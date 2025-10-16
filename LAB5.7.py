import re

def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

text = "this_is_snake_case"
print(snake_to_camel(text))
