class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)


        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for x in range(k+1,n):
                        if (nums[i] + nums[j] + nums[k] + nums[x]) == target:
                            curr = [nums[i], nums[j], nums[k], nums[x]]
                            curr.sort()
                            res.add(tuple(curr))


        return [list(tup) for tup in res] 