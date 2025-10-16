import re

text = "abc_def ghi_jkl mn_op qr_st uv"
result = re.findall(r'[a-z]+_[a-z]+', text)
print(result)
