class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        start1 = start2 = 0
        while start1 < len(haystack) - len(needle) + 1:
            pos = start1
            while start2 < len(needle) and haystack[start1] == needle[start2]:
                start1 += 1
                start2 += 1
            if start2 == len(needle):
                return pos
            start2 = 0
            start1 = pos+1
        return -1