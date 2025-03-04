class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for item in nums:
            count = nums.count(item)
            if count > 1:
                for _ in range(count-1):
                    nums.remove(item)

        return len(nums)