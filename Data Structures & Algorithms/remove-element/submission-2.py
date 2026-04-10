class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        l,r = 0,len(nums)- 1 

        while l <= r:
            if nums[l]== val:
                nums[r],nums[l] = nums[l],nums[r]
                k -= 1 
                r -= 1 
            else:
                l += 1
        return k