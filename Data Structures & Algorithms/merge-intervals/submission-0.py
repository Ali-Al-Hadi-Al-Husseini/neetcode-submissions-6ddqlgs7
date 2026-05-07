class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        result = []
        idx = 0

        while idx < len(intervals):
            merged_interval = intervals[idx]
            mergeable = False
            if idx +1  < len(intervals):
                mergeable = merged_interval[1] >= intervals[idx+1][0]

            while mergeable:
                merged_interval = [min(merged_interval[0],intervals[idx+1][0]), max(merged_interval[1],intervals[idx+1][1])]
                idx += 1
                if idx +1  >= len(intervals):
                    break
                mergeable = merged_interval[1] >= intervals[idx+1][0]
            
            result.append(merged_interval)
            idx += 1
        return result