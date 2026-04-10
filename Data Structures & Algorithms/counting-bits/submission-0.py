class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = {}
        return count_bits_helper(n,memo)




def count_bits_helper(n,memo):
    if n <= 0: return [0]
    if n in memo: return memo[n]
    memo[n] = count_bits_helper(n - 1,memo)
    memo[n].append(get_bits_count(n))

    return memo[n]

def get_bits_count(n):
    bits_count = 0

    while n >0:
        if n & 1 == 1 :
            bits_count += 1

        n >>=1

    return bits_count
