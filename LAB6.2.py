def count_case(string):
    upper = sum(1 for c in string if c.isupper())
    lower = sum(1 for c in string if c.islower())
    return upper, lower

text = "Hello World!"
upper, lower = count_case(text)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")