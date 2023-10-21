class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        start = 0
        end = len(s)-1
        result = list(s)
       

        while start < end :
            while start < end and result[start] not in vowels:
                start+=1

            while start < end  and result[end] not in vowels:
                end -= 1


            temp = result[start]
            result[start] = result[end]
            result[end] = temp

            start +=1
            end -= 1
        return "".join(result)