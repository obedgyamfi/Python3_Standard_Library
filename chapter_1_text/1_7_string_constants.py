# 1.7: string_constants.py
#       The formatter class implements the same layout 
#       specification language as format() method of str.
#       Most of the time format() method is more convenient
#       but Formatter is provided as a way to build subclass
#       for cases where variations are needed.

#   The string module includes a number of constants related to 
#   ASCII and numerical character sets.

import inspect
import string

def is_str(value):
    return isinstance(value,str)

for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))