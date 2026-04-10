class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        idx = 0 
        while idx < len(nums):
            if nums[idx] == val:
                del nums[idx]
                k -= 1 
                idx -= 1

            idx += 1

        return k