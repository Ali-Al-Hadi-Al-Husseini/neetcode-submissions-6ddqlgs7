class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        bin_count = [[0,0] for st in strs]

        for idx,st in enumerate(strs):
            for _bit in st:
                if _bit == "1":
                    bin_count[idx][1] += 1
                elif _bit == "0":
                    bin_count[idx][0] += 1

        table = [[[0]* (n+1) for _ in range(m+1)] for _ in range(len(strs) + 1)]

        for i in range(1,len(strs)+1):
            for j in range(m+1):
                for k in range(n+1):
                    zeros,ones = bin_count[i-1]
                    table[i][j][k] = table[i-1][j][k]
                    if j - zeros >= 0  and k - ones >= 0 :
                        table[i][j][k] = max(table[i][j][k],table[i-1][j - zeros][k - ones] + 1)

        return table[len(strs)][m][n]



