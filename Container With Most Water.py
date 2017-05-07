# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        area = 0
        while start < end:
            if height[start] < height[end]:
                area = max(area, (end-start)*height[start])
                start += 1
            else:
                area = max(area, (end-start)*height[end])
                end -= 1
        return area

a = Solution()
b = a.maxArea([1,2,3,4,5,6])
print(b)
