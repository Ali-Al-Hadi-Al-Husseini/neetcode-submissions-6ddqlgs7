class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        robbed = set()

        def helper(idx,lim):
            if idx == 4:
                print('hola')
            if idx in robbed or idx >= lim :
                return  0

            if idx in memo :
                return memo[idx]

            robbed.add(idx)
            robbed_with = helper((idx +2),lim ) + nums[idx]
            robbed.remove(idx)
            robbed_without = helper(idx+1,lim)
            memo[idx] = max(robbed_without,robbed_with)
            return memo[idx]
        first_part = helper(1 ,len(nums))
        robbed = set()
        memo = {}
        return max(first_part,helper(0,len(nums) -1),nums[0])