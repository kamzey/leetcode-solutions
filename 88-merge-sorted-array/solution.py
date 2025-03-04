class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # nums1 index
        j = n - 1 # nums2 index
        k = m + n - 1 # filling index

        while j>=0: # while nums2 is not exhausted
            if i>=0 and nums1[i] > nums2[j]: # while nums1 is not exhausted
                nums1[k] = nums1[i]
                i -= 1 # time to fill next one
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1