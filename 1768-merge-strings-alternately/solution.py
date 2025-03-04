class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_string = ""
        small = min(len(word1),len(word2))
        big = max(len(word1),len(word2))
        for i in range(small):
            new_string = new_string + word1[i]
            new_string = new_string + word2[i]
        for i in range(small,big):
            if len(word1)>=len(word2):
                new_string = new_string + word1[i]
            else:
                new_string = new_string + word2[i]
        return new_string
