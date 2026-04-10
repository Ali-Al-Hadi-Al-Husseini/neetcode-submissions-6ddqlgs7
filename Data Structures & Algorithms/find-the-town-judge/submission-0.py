class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = trust[0][1]

        for trss in trust:
            if trss[1] != trusted:
                return -1
        
        return trusted