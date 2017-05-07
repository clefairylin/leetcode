class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        cur = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == target:
                    return sums
                if abs(cur-target) > abs(sums-target):
                    cur = sums

                if sums < target:
                    j += 1
                elif sums > target:
                    k -= 1
        return cur
