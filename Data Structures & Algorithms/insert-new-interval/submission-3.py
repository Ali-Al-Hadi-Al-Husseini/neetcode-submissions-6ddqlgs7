class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx =0
        while idx < len(intervals) and newInterval[0] > intervals[idx][0]:
            idx += 1 
            
        
        
        new_pos = idx
        merged_interval = newInterval
        while idx > 0 and intervals[idx - 1][1] >= merged_interval[0]:
            merged_interval = merge_interval(merged_interval,intervals[idx - 1])
            intervals.pop(idx-1)
            idx -= 1

        while idx  < len(intervals) and merged_interval[1] >= intervals[idx][0]:
            merged_interval = merge_interval(merged_interval,intervals[idx])
            intervals.pop(idx)

        intervals.insert(idx,merged_interval)
        return intervals


def merge_interval(inter1, inter2):
    start = min(inter1[0],inter2[0])
    end = max(inter1[1],inter2[1])
    return [start,end]