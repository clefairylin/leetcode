class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        swap_index = -1
        for i in range(-1, -len(nums), -1):
            if nums[i] > nums[i-1]:
                swap_index = i-1
                break

        for min_index in range(-1, -len(nums)-1, -1):
            if nums[swap_index] < nums[min_index]:
                nums[swap_index], nums[min_index] = nums[min_index], nums[swap_index]
                nums[swap_index + 1:] = sorted(nums[swap_index+1:])
                break