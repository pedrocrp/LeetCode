class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ''
        if len(word2) > len(word1):
            for i in range(len(word1)):
                final += word1[i] + word2[i]
            final += word2[len(word1):]
        else:
            for i in range(len(word2)):
                final += word1[i] + word2[i]
            final += word1[len(word2):]
        
        return final