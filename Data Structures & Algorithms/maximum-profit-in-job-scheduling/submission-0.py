from functools import cache 
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime,endTime,profit))


        @cache
        def helper(i):
            if i >= len(intervals):
                return 0

            dont_include = helper(i +1)

            j = i + 1
            while j < len(intervals):
                if intervals[i][1] <= intervals[j][0]:
                    break
                j += 1

            return max(dont_include,intervals[i][2] + helper(j))

        return helper(0)