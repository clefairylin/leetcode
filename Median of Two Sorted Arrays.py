class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        qua = (n+m)/2.0
        v = c1 = c2 = 0
        if (m+n) % 2 == 0:
            while c1+c2 < qua:
                if c1 == n:
                    v = nums2[c2]
                    c2 += 1
                elif c2 == m:
                    v = nums1[c1]
                    c1 += 1
                elif nums1[c1] <= nums2[c2]:
                    v = nums1[c1]
                    c1 += 1
                else:
                    v = nums2[c2]
                    c2 += 1
            if c1 == n:
                v1 = nums2[c2]
            elif c2 == m:
                v1 = nums1[c1]
            else:
                v1 = min(nums1[c1], nums2[c2])
            return (v + v1)/2.0
        else:
            while c1+c2 < int(qua+1):
                if c1 == n:
                    v = nums2[c2]
                    c2 += 1
                elif c2 == m:
                    v = nums1[c1]
                    c1 += 1
                elif nums1[c1] <= nums2[c2]:
                    v = nums1[c1]
                    c1 += 1
                else:
                    v = nums2[c2]
                    c2 += 1
            return v