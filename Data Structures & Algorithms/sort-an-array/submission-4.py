class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge_sort(l,r):
            if l>=r :
                return  

            m = (l + r ) // 2 
            merge_sort(l,m)
            merge_sort(m+1,r)


            left,right = nums[l:m+1],nums[m+1:r+1]
            i,j,k= 0 , 0 , l 

            while i < len(left) and j <len(right):
                if left[i] >= right[j]:
                    nums[k] = right[j]
                    j +=1
                else:
                    nums[k] = left[i]
                    i += 1 

                k += 1

            while i <len(left):
                nums[k] = left[i]
                i+= 1
                k+=1

            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1

            
        merge_sort(0,len(nums) -1 )
        return nums