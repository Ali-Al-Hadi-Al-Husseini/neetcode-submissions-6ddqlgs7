class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_dict = {}


        for trst in trust:
            if trst[0] not in trusts_dict:
                trusts_dict[trst[0]] = []
            trusts_dict[trst[0]].append(trst[1])

        
        trusted_by_dict = {}
        max_trusted = trust[0][1]

        for trst in trust:
            if trst[1] not in trusted_by_dict:
                trusted_by_dict[trst[1]] = []

            trusted_by_dict[trst[1]].append(trst[0])            
            max_trusted = max(trst[1],max_trusted,key=lambda x:len(trusted_by_dict[x]))

        if max_trusted not in trusts_dict and n -1 <=len(trusted_by_dict[max_trusted]):
            return max_trusted
        else:
            return -1
