from functools import cache 
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime,endTime,profit))


        @cache
        def helper(i):
            if i >= len(intervals):
                return 0

            dont_include = helper(i +1)

            left,right= i +1 , len(intervals) 
            j = right
            while left < right:
                mid = (left + right) // 2 
                if intervals[mid][0] >= intervals[i][1]:
                    j = mid 
                    right = mid 
                else :
                    left = mid + 1

            return max(dont_include,intervals[i][2] + helper(j))

        return helper(0)