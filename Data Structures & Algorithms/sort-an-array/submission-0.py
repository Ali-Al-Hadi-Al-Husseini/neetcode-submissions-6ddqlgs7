class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge_sort(arr):
            if len(arr) == 1 :
                return arr 

            mid = len(arr) // 2 
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            new_arr = []
            i,j = 0,0

            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    new_arr.append(right[j])
                    j += 1 
                else:
                    new_arr.append(left[i])
                    i += 1

            if i < len(left):
                new_arr.extend(left[i:])
            elif j < len(right):
                new_arr.extend(right[j:])
            return new_arr



        return merge_sort(nums)