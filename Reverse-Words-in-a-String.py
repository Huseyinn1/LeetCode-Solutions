class Solution(object):
    def reverseWords(self, s):
        
        words = s.split()

        words = words[::-1]

        reverse = ' '.join(words)
        
        return reverse