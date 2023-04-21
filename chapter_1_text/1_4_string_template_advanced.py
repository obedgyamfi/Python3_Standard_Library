# 1.4: string_template_advanced.py
#   string.Template can be changed by adjusting the regular expression patterns
#   it uses to find the variable names in template body. A simple way to do that
#   is to change the delimiter and idpattern class attributes.

import string

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
    Delimiter : %%
    Replaced  : %with_underscore
    Ignored   : %notounderscored
'''
d = {
    'with_underscore': 'replaced',
    'notundersocred' : 'not replaced'
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))


