class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head, end = 0, len(nums)-1
        while head <= end:
            mid = (head + end) // 2
            if nums[mid] == target:
                return mid
            if nums[head] <= nums[mid]:
                if nums[head] <= target < nums[mid]:
                    end = mid - 1
                else:
                    head = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    head = mid + 1
                else:
                    end = mid - 1
        return -1
