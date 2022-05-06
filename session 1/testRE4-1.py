import re

text="image.png"

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
[^0-9] any character except a digit
\D <=> [^0-9]
\s <=> white space
^   beginning of the string
$   end the string
(gif|jpg|png)   gif or jpg or png
"""

regexp=re.compile(r"^(.+)\.(gif|jpg|png)$")

matchobj=regexp.search(text)
if matchobj:
    print("The string text 'match'")
# =============================================================================
    print(matchobj.groups())

# =============================================================================
else:
    print("The string text does not 'match'")