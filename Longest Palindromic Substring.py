# -*- coding:utf-8 -*-


s = 'aaaaaa'

target_s = ''
length = 0
s = '#' + s + '*'
for i in range(1, len(s)-1):
    j = 1
    if s[i] == s[i+1]:
        while s[i-j] == s[i+j+1]:
            j += 1
        if 2*j >= length:
            length = 2*j
            target_s = s[i-j+1:i+j+1]
        continue
for i in range(1, len(s) - 1):
    j = 1
    while s[i-j] == s[i+j]:
        j += 1
    if 2*j - 1 >= length:
        length = 2*j - 1
        target_s = s[i-j+1:i+j]
    continue
print(target_s)

