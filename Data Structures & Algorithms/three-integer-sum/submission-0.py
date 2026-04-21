class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum = defaultdict(set)
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i +1,len(nums)):
                curr_sum = nums[i] + nums[j]
                two_sum[0 - curr_sum].add((i,j))

        for idx in range(len(nums)):
            if  nums[idx] in two_sum:
                for i,j in two_sum[ nums[idx]]:
                    if idx == i or idx == j:
                        continue
                    tmp = [nums[idx], nums[i], nums[j]]
                    tmp.sort()
                    res.add(tuple(tmp))

        return [list(tup) for tup in res]
