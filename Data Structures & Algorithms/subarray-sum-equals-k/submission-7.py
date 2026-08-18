class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_freq = defaultdict(int)
        prefix_freq[0] = 1 
        res = 0
        prefix_sum = 0

        for idx in range(len(nums)):
            prefix_sum += nums[idx]
            diff = prefix_sum - k 

            res += prefix_freq[diff]
            prefix_freq[prefix_sum] += 1 

            


        return res

