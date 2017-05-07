# -*- coding: utf-8 -*-


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # T = ['', 'M', 'MM', 'MMM']
        # H = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        # D = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        # U = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        # thousand = num//1000
        # hundred = (num - thousand*1000)//100
        # decade = (num - thousand*1000 - hundred*100)//10
        # unit = num - thousand*1000 - hundred*100 - decade*10
        # roma = T[thousand] + H[hundred] + D[decade] + U[unit]
        # return roma

        roma = ''
        thousand = num // 1000
        hundred = (num - thousand * 1000) // 100
        decade = (num - thousand * 1000 - hundred * 100) // 10
        unit = num - thousand * 1000 - hundred * 100 - decade * 10

        roma += thousand * 'M'
        if hundred == 9:
            roma += 'CM'
        elif hundred == 4:
            roma += 'CD'
        elif 5 <= hundred <= 8:
            roma = roma + 'D' + 'C' * (hundred - 5)
        else:
            roma += 'C' * hundred
        if decade == 9:
            roma += 'XC'
        elif decade == 4:
            roma += 'XL'
        elif 5 <= decade <= 8:
            roma = roma + 'L' + 'X' * (decade - 5)
        else:
            roma += 'X' * decade
        if unit == 9:
            roma += 'IX'
        elif unit == 4:
            roma += 'IV'
        elif 5 <= unit <= 8:
            roma = roma + 'V' + 'I' * (unit - 5)
        else:
            roma += 'I' * unit
