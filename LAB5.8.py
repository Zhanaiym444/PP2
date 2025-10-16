import re

text = "SplitAtUpperCaseLettersExample"
result = re.split(r'(?=[A-Z])', text)
print(result)
