class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        y = len(str1)
        x = len(str2)

        while y:
            x, y = y, x % y
            
        len_str = abs(x)

        d1 = len(str1) / len_str
        d2 = len(str2) / len_str
        gcd = ""

        for i in range(len_str):
            if d1 * str1[0:len_str-i] == str1 and d2 * str1[0:len_str-i] == str2:
                gcd = str1[0:len_str-i]

        return gcd

            