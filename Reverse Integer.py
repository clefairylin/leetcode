# -*- coding: utf-8 -*-


x = 1534236469

if x >= 0:
    s = str(x)
    new_x = int(s[::-1])
else:
    s = str(-x)
    new_x = int(s[::-1])*(-1)

if new_x > 4294967295:
    print(0)
else:
    print(new_x)

