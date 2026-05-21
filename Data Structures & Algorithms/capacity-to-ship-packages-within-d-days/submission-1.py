class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left,right = max(weights), sum(weights)
        least_capcity = right
        while left <= right:
            mid_capcity = (left + right) // 2 
            curr_days = packing_time(weights,mid_capcity)

            if curr_days > days:
                left = mid_capcity  + 1
            else:
                least_capcity = min(least_capcity,mid_capcity)
                right = mid_capcity  -1 

        return least_capcity



def packing_time(weights,curr_capcity):
    days = 0
    curr_package = 0

    for weight in weights:
        if curr_package + weight > curr_capcity:
            days += 1
            curr_package = 0
            
        curr_package += weight

    return days + ( 1 if curr_package >0 else 0)





