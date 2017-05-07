class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        # s = s.replace('IV', 'IIII')
        # s = s.replace('V', 'IIIII')
        # s = s.replace('IX', 'IIIIIIIII')
        # s = s.replace('XL', 'XXXX')
        # s = s.replace('L', 'XXXXX')
        # s = s.replace('XC', 'XXXXXXXXX')
        # s = s.replace('CD', 'CCCC')
        # s = s.replace('D', 'CCCCC')
        # s = s.replace('CM', 'CCCCCCCCC')
        # for i in s:
        #     num += val[i]

        for i in range(len(s)-1):
            if val[s[i]] < val[s[i+1]]:
                num -= val[s[i]]
            else:
                num += val[s[i]]
        return num + val[s[len(s)-1]]
