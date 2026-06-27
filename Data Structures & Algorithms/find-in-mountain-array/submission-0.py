class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        top = find_mountain_top(mountainArr)
        left_side = binary_search(0,top,mountainArr,target,True)
        if left_side != -1 :
            return left_side
        return binary_search(top,mountainArr.length() - 1,mountainArr,target,False)

def binary_search(left,right,arr,target,inc):

    while left<= right:
        mid = (left+right) // 2
        mid_val = arr.get(mid)

        if mid_val ==  target:
            return mid 

        elif inc:
            if mid_val > target:
                right = mid -1 
            else:
                left = mid + 1
        else:
            if mid_val > target:
                left = mid +1
            else:
                right = mid -1 


    return -1 


def find_mountain_top(arr):
    left,right = 0, arr.length() -1 
    
    while left <= right:
        mid = (left + right) // 2 
        if arr.get(mid-1) > arr.get(mid) > arr.get(mid+1):
            right = mid 
        elif arr.get(mid-1) < arr.get(mid) < arr.get(mid+1):
            left = mid 

        else:
            return mid 
