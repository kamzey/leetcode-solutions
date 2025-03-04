class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        result = [True if candies[i] + extraCandies >= max(candies) else False for i in range(len(candies))]
        return result