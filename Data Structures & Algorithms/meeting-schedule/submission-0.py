"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda a:a.start)

        last_inter = Interval(float("-inf"),float("-inf"))
        for inter in intervals:
            if last_inter.end > inter.start:
                return False

            last_inter = inter

        return True 
