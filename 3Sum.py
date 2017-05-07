class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums = sorted(nums)

        if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
            return []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i+1, len(nums)-1
            while start < end:
                sum = nums[start] + nums[end] + nums[i]
                if sum == 0:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif sum > 0:
                    end -= 1
                else:
                    start += 1
        return list(map(list, res))
