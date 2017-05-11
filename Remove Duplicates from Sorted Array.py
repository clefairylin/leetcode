class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, length = 0, 0
        nums.append("*")
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                nums[length] = nums[i]
                length += 1
            i += 1
        return length