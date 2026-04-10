class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <2: return strs[0]
        curr_prefix = has_prefix(strs[0],strs[1])

        for idx in range(2,len(strs)):
            new_prefix = has_prefix(strs[idx],strs[idx - 1])
            not_similar_prefix =  new_prefix not in curr_prefix and curr_prefix not in new_prefix
            if new_prefix == "" or not_similar_prefix:
                return ""
            if len(new_prefix) < len(curr_prefix):
                curr_prefix = new_prefix

            
        return curr_prefix




def has_prefix(word1,word2):
    least_length = min(len(word1),len(word2))
    prefix = []

    for idx in range(least_length):
        if word1[idx] == word2[idx]:
            prefix.append(word1[idx ])   
        else:
            break

    return "".join(prefix)