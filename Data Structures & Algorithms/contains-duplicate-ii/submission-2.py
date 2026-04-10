class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupes = {}

        for idx,num in enumerate(nums) :
            if num in dupes:
                if abs(idx - dupes[num]) <= k: 
                    return True 
            dupes[num] = idx

        return False