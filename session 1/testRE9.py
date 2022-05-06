# -*- coding: utf-8 -*-
"""
VERBOSE Flag
"""
import re

text="Amazon is a GAFA"

regexp=re.compile(r"""
                        ^         # The beginning of the text
                        ([abc])   # first character (must be a or b or c)
                        (.+)      # the rest of the string (except the last char)
                        ([abc])   # last character (must be a or b or c)
                        $         # The end of the regexp
                        """, re.VERBOSE|re.IGNORECASE)
 # <=> "^([abc])(.+)([abc])$"
  
matchobj=regexp.search(text)

if matchobj:
    print("The string text 'match'")
    print(matchobj.groups())
else:
    print("The string text does not 'match'")