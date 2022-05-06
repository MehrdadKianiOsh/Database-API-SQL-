import re

text="value +23.45 the end"

"""
\d     a digit
+         1 or more occurrence
{min,max} between [min,max] occurrences
{2,}    2 or more occurrences
{3}     3 occurrences
{1,} <=> +
{0,} <=> *
{0,1} <=> ?
.    any character except a new line
\.   the character .
[123]
\d <=> [0123456789]
\d <=> [0-9]
"""

regexp=re.compile(r"([+-]?(\d+)\.(\d+))")

matchobj=regexp.search(text)
if matchobj:
    print("The string text 'match'")
    print(matchobj.groups())
    print(matchobj.group(1))
    print(matchobj.group(2))
    print(matchobj.group(3))

else:
    print("The string text does not 'match'")