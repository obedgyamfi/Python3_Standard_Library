# 1.2: string_template.py
#       With string.Template interpolation, variables are 
#       identified by prefixing the name with $.
#       This example compares a simple template with similar string 
#       interpolation using the operator and the new format string syntax using
#       str.format()

import string

values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))