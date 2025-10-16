import re

text = "Python JavaScript Cplusplus HTML css GoLang"
result = re.findall(r'[A-Z][a-z]+', text)
print(result)
