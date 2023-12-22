class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        minValue = min(len(str1),len(str2))
        i = 1
        string = ''
        while i <= minValue:
            if str1[0:i] == str2[0:i] and (len(str1)%i == 0) and (len(str2)%i == 0):
                string = str1[0:i]
            i += 1
        
        if (str1.count(string) * string) == str1 and (str2.count(string) * string) == str2:
            return string
        else:
            return ''