class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {key:[] for key in t}

        for idx, _char in enumerate(t):
            memo[_char].append(idx)

        last_idx = 0
        for _char in s :
            if _char not in memo: return False

            curr_idx = memo[_char].pop(0)
            while curr_idx < last_idx:
                if len(memo[_char]) == 0: return False
                curr_idx = memo[_char].pop(0)

            last_idx = curr_idx

            if len(memo[_char]) == 0:
                del memo[_char]

        return True
        