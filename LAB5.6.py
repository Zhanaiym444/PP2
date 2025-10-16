import re

text = "Python, is. awesome language"
result = re.sub(r'[ ,.]', ':', text)
print(result)
