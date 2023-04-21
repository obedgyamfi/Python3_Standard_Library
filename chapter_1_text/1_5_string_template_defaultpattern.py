# 1.5: string_template_defaultpattern.py
#       It is possible to override the pattern attribute and define an entirely
#       new regular expression. 
#       The pattern must have four groups for capturing escpaed delimiter, the 
#       named variable, a braced version of variable name, invalid delimiter.

import string

t = string.Template('$var')
print(t.pattern.pattern)