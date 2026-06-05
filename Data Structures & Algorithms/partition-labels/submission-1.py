class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices = {s[i]:i for i in range (len(s))}

        res = []
        length = 0
        last_idx_needed = 0

        for idx in range(len(s)):
            length += 1
            last_idx_needed = max(last_idx_needed,last_indices[s[idx]])

            if idx == last_idx_needed:
                res.append(length)
                length = 0 

        return res 