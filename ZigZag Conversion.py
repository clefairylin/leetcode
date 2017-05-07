# -*- coding:utf-8 -*-


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = []
        use = []
        count = 0
        for i in range(numRows):
            use.append([])

        for cha in s:
            if count == numRows:
                count = -2
            if count == -(numRows+1):
                count = 1
            use[count].append(cha)
            if count >= 0:
                count += 1
            else:
                count -= 1

        for l in use:
            zigzag.extend(l)

        return "".join(zigzag)
