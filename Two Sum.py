# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        status = False
        for i in range(len(nums)):
            index_1 = i
            rem = target - nums[i]
            if rem in nums:
                for j in range(len(nums)):
                    if j == i:
                        continue
                    if nums[j] == rem:
                        index_2 = j
                        status = True
            if status is True:
                break
        return list((index_1, index_2))
