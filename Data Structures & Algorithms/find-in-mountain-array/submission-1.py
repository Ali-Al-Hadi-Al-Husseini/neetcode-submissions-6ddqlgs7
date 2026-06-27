class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        cache = {}
        def get(idx):
            if idx not in cache:
                cache[idx] = mountainArr.get(idx)
            return cache[idx]

        top = find_mountain_top(get,mountainArr.length())
        left_side = binary_search(0,top,get,target,True)
        if left_side != -1 :
            return left_side
        return binary_search(top,mountainArr.length() - 1,get,target,False)

def binary_search(left,right,get,target,inc):

    while left<= right:
        mid = (left+right) // 2
        mid_val = get(mid)

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


def find_mountain_top(get,length):
    left,right = 0, length -1 
    
    while left <= right:
        mid = (left + right) // 2 
        if get(mid-1) > get(mid) > get(mid+1):
            right = mid 
        elif get(mid-1) < get(mid) < get(mid+1):
            left = mid 

        else:
            return mid 
