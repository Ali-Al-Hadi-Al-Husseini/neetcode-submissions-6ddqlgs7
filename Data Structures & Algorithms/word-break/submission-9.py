class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def helper(curr_word):
            if curr_word == s:
                return True
            if len(curr_word) >= len(s):
                return False 
            if curr_word in memo:
                return memo[curr_word]

            for word in wordDict:
                if curr_word + word not in s :
                    continue
                memo[curr_word + word] = helper(curr_word+word)
                if memo[curr_word + word] == True:
                    return True

            return False
        
        return helper('')
