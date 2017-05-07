# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = {}
        length = start = 0
        for i in range(len(s)):
            if s[i] not in cur:
                length = max(length, i-start+1)
            elif start > cur[s[i]]:
                length = max(length, i-start+1)
            else:
                whe = cur[s[i]]
                start = whe + 1
            cur[s[i]] = i
        return length
