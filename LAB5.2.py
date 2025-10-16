import re

pattern = r'ab{2,3}'
texts = ['a', 'abb', 'abbb', 'abbbb', 'ab']

for text in texts:
    if re.fullmatch(pattern, text):
        print(text)
