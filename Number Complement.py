# -*- coding: utf-8 -*-


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(int(num)).replace('0b', '')
        new_num = ''
        for i in num:
            print(new_num)
            if i == '0':
                new_num = new_num + '1'
            else:
                new_num = new_num + '0'
        print(new_num)
        return int(new_num, 2)

a = Solution()
b = a.findComplement(2)
print(b)