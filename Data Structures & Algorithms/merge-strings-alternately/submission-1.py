class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []

        length = min(len(word1),len(word2))
        word1_is_longer = True if len(word1) > len(word2) else False 
        for i in range(length):
            res.append(word1[i])
            res.append(word2[i])

 
        res.extend(word1[i+1:])
        res.extend(word2[i+1:])


        
        return "".join(res)