class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)
        hash_map = {target -num :idx for idx,num in enumerate(nums)}
        

        

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                        if (nums[i] + nums[j] + nums[k]) not in hash_map:
                            continue
                        idx = hash_map[(nums[i] + nums[j] + nums[k])]
                        if idx != i and idx != j and idx != k:
                            curr = [nums[i], nums[j], nums[k],nums[idx] ]
                            curr.sort()
                            res.add(tuple(curr))


        return [list(tup) for tup in res] 