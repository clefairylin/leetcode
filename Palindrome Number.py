# -*- coding: utf-8 -*-

x = 121
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # digit = 1
        # reverse_x = 0
        # x1 = x
        # while x // 10**digit > 0:
        #    digit += 1
        # for i in range(1, digit+1):
        #    reverse_x += 10**(i-1) * (x1 // 10**(digit-i))
        #   x1 %= (10**(digit-i))
        # if reverse_x == x:
        #   return True
        # else:
        #    return False

        s = str(x)
        l = len(s)
        if l == 1:
            return True
        if l % 2 != 0:
            mid = l // 2
            for i in range(1, mid + 1):
                if s[mid - i] != s[mid + i]:
                    return False
        else:
            for i in range(int(l / 2)):
                if s[i] != s[-(i + 1)]:
                    return False
        return True
