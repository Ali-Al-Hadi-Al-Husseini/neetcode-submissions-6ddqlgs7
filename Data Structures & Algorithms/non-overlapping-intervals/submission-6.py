class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        merged_intervals = 0
        idx = 1

        while idx < len(intervals):
            j = idx - 1
            prev = intervals[j]
            if prev[0] == None:
                j = prev[1]
                prev = intervals[j]
                
            curr = intervals[idx]
            if prev[1] > curr[0]:
                merged_intervals += 1 
                if curr[1]  < prev[1]:
                    prev[0] = None
                    prev[1] = j
                else:
                    curr[0] = None
                    curr[1] = j

            idx += 1 

        return merged_intervals
