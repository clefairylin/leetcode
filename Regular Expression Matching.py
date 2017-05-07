# -*- coding: utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        status = [[False]*(len(s)+1) for i in range(len(p)+1)]
        status[0][0] = True
        for i in range(2, len(p)+1):
            status[i][0] = p[i-1] == '*' and status[i-2][0]
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    status[i][j] = status[i - 2][j] or ((p[i-2] == '.' or p[i-2] == s[j-1]) and status[i][j-1])
                else:
                    status[i][j] = (p[i-1] == '.' or p[i-1] == s[j-1]) and status[i-1][j-1]
        return status[-1][-1]