class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans, sign = 0, 1
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            sign = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            temp, cache = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += cache
                temp *= 2
                cache *= 2
        if sign == 0:
            return min(ans, 2147483647)
        else:
            return max(-ans, -2147483648)