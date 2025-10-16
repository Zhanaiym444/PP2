import re

pattern = r'a.*b$'
texts = ['acb', 'a123b', 'a-b', 'ab', 'axxx', 'b']

for text in texts:
    if re.fullmatch(pattern, text):
        print(text)
