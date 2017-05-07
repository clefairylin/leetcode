class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {"(": 1, "{": 2, "[": 3}
        right = {")": 1, "}": 2, "]": 3}
        if len(s) == 0 or len(s) % 2 != 0 or s[0] in right or s[-1] in left:
            return False
        start = 0
        while start < len(s):
            if s[start] in left:
                start += 1
                continue
            elif s[start] in right:
                if right[s[start]] == left[s[start-1]]:
                    s = s[:start-1] + s[start+1:]
                    start -= 1
                    continue
                else:
                    return False
        if s:
            return False
        else:
            return True