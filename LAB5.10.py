import re

def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')

text = "camelCaseStringExample"
print(camel_to_snake(text))
