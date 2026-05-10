class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def helper(idx):
            if idx == len(s):
                return True
            if idx in memo:
                return memo[idx]
            # if idx > len(s):
            #     return False

            for word in wordDict:

                if word != s[idx:idx +len(word)]:
                    continue
                new_idx = idx + len(word)
                print(new_idx,s[idx:])

                memo[new_idx] = helper(new_idx)
                if memo[new_idx] == True:
                    return True

            return False
        
        return helper(0)
