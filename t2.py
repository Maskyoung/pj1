# /usr/bin/env python
# -*- coding: utf-8 -*-
# a = 7
# if a > 0:
#     # raise ValueError('number must be non-negative')
#     print('asd')
# else:
#     print(a)
#
# # # print(a)
# s='asdga\asdgasdasd\sdg\t\t'
# print(s)
# import re
# def plural(noun):
#     if re.search('[sxz]$', noun):
#         return re.sub('$', 'es', noun)
#     elif re.search('[^aeioudgkprt]h$', noun):
#         return re.sub('$', 'es', noun)
#     elif re.search('[^aeiou]y$', noun):
#         return re.sub('y$', 'ies', noun)
#     else:
#         return noun + 's'
# print(plural('asdngoasdcnaois'))

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b