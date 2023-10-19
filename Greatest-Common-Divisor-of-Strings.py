class Solution(object):
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    @classmethod
    def gcdOfStrings(self, str1, str2):
        
        if str1 + str2 != str2 + str1:
            return ""
        divisor_length = Solution.gcd(len(str1),len(str2))
        return str1[:divisor_length]
