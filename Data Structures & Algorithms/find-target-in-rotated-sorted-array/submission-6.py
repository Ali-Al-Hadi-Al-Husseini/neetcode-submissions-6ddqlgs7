class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums)  - 1 

        while left <= right:
            mid = (left + right) // 2 

            if nums[mid] == target:
                return mid

            elif nums[left] < nums[right]:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1 
            else:
                if nums[right] >= target:
                    left += 1
                else:
                    right -= 1

        return - 1
