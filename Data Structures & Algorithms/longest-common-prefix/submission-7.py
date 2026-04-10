class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for idx,word in enumerate(strs):
            j = 0 
            for j , _char in enumerate(word):
                if len(prefix) > j and prefix[j] != _char:
                    break
                j += 1

            prefix = prefix[:j]

        return prefix