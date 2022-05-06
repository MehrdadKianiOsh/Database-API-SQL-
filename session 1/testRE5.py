import re

text="123 56:678   789;;897"

"""
split()
"""


regexp=re.compile(r"[;:\s]+")

result=regexp.split(text)

print(result)
   