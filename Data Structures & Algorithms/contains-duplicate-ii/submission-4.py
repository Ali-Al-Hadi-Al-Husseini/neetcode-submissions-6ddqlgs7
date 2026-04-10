class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = 0

        while idx < len(nums):
            old_idx = idx # 0 
            
            while idx <= (old_idx + k )  and idx < len(nums):
                if nums[old_idx] == nums[idx] and abs(old_idx - idx) <= k and idx != old_idx:
                    return True
                idx += 1 

            idx = old_idx + 1 

        return False
                    