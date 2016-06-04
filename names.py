#!/usr/bin/python

def namelist(names):
    num_args = len(names)
    if num_args == 1:
      return names[0]['name']
    elif num_args == 2:
      return names[0]['name'] + ', ' + names[1]['name']
    elif num_args > 2:
      ret_str = names[0]['name'] + ', '
      i = 1
      while i < num_args-2:
        ret_str += names[i]['name'] + ', '
        i += 1
      else:
        ret_str += '&' + names[i]['name']
    else:
      return ''

namelist_arg = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

output = namelist(namelist_arg)
print output
