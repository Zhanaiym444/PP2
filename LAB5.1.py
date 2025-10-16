import re

pattern = r'ab*'  # a+любое количество 'b'
texts = ['a', 'ab', 'abb', 'ac', 'b', 'aab']

for text in texts:
    if re.fullmatch(pattern, text):
        print(text)
