# 1.3:string_template_missing.py
#       The use of safe_subtitute() method makes it possible to avoid exceptions 

import string

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute()      :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitute():', t.safe_substitute(values))