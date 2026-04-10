class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate,count = 0 ,0

        for num in nums:
            if count <= 0:
                candidate = num
            
            count += (1 if candidate == num else -1)
            print(count)
            print(candidate)
        return candidate 