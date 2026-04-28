class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        left,right = 1, max(piles)
        min_speed = float("inf")

        while left <= right:
            mid = (left+ right ) // 2 

            curr_time = find_time(mid,piles[:])
            if curr_time <= h:
                min_speed = min(mid, min_speed)
            print(curr_time)
            if  curr_time > h:
                left = mid + 1 
            else : 
                right = mid - 1

        return min_speed






def find_time(speed,piles):
    curr_time= 0


    for  pile in piles:
        time_needed = (pile // speed)
        curr_time += time_needed + (0 if pile% speed == 0 else  1)


    return curr_time