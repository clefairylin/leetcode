# -*- coding: utf-8 -*-


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        bin_x = bin(x).replace('0b', '')
        bin_y = bin(y).replace('0b', '')
        len_x = len(bin_x)
        len_y = len(bin_y)
        if len_x > len_y:
            for i in range(len_x - len_y):
                bin_y = '0' + bin_y
            for i in range(len_x):
                if bin_x[i] != bin_y[i]:
                    count += 1
        else:
            for i in range(len_y - len_x):
                bin_x = '0' + bin_x
            for i in range(len_y):
                if bin_x[i] != bin_y[i]:
                    count += 1
        return count

'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x).replace('0b', '')
        bin_y = bin(y).replace('0b', '')
        for i in range(32-len(bin_x)):
            bin_x = '0' + bin_x

        for i in range(32-len(bin_y)):
            bin_y = '0' + bin_y

        count = 0
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                count += 1
        return count
'''