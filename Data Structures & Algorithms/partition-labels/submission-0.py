class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars_freq = defaultdict(int)

        for _chr in s:
            chars_freq[_chr] += 1 

        res = []
        last_sub_strig = -1
        _map = {}
        for i in range(len(s)):
            if len(_map) > 0 or chars_freq[s[i]] > 1:
                chars_freq[s[i]]-= 1
                _map[s[i]] = chars_freq[s[i]]
                if _map[s[i]] == 0 :
                    del _map[s[i]] 
                if len(_map) > 0 :
                    continue 
            last_sub_set = set()
            res.append(i - last_sub_strig )
            last_sub_strig = i 
            del chars_freq[s[i]]
        return res 
