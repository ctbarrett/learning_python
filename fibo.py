#!/usr/local/bin/python3

def get_fib(n):
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)
    a, b = b, a+b
  return result

def fib(n, type):
    if type == 'string':
        print(' '.join(map(str,get_fib(n))))
    elif type == 'list':
        return get_fib(n)
    else:
        raise 'TypeError: Invalid Return Type: ' + type + '!'

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]), 'string')
