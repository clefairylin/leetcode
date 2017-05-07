class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target2 = target-nums[i]
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                start, end = j+1, len(nums)-1
                target3 = target2 - nums[j]
                while start < end:
                    if nums[start] + nums[end] == target3:
                        res.add((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                    elif nums[start] + nums[end] < target3:
                        start += 1
                    else:
                        end -= 1
        return list(map(list, res))