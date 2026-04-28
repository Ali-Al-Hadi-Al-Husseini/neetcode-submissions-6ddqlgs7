class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) -1 
        #[5,6,7,0,1,2,3]
        #[4,5,6,7,0,1,2]
        # [1,3,5]
        while left <= right:
            mid = (left+ right ) // 2 

            if nums[mid] == target:
                return mid

            if target > nums[mid]:

                if target <= nums[right] or nums[mid] > nums[left] :
                    left = mid  + 1
                    

                else:
                    print("went left")
                    right = mid - 1 
            else:
                if target >= nums[left] or nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1



        return -1