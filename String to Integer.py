# -*- coding: utf-8 -*-


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        target = []
        num = sign = False
        for i in str:
            if i == " " and num is False:
                continue
            elif i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                target.append(i)
                num = True
            elif i == "-" or i == "+":
                if sign is False:
                    sign = i
                    num = True
                else:
                    target = []
                    break
            else:
                break

        if target:
            res = int("".join(target))
            if sign == "-":
                if res < 2147483648:
                    return -res
                else:
                    return -2147483648
            else:
                if res < 2147483647:
                    return res
                else:
                    return 2147483647
        else:
            return 0
