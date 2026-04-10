class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
            dupes = set()
            l = 0 
            # l = 1 r = 2 
            # dupes  {1,0,
            for r in range(len(nums)):
                if r - l  > k:
                    dupes.remove(nums[l])
                    l += 1 
                if r - l <= k and nums[r] in dupes:
                    return True
                dupes.add(nums[r])

            return False 

                
                    