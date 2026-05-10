    """
    Definition of Interval:
    class Interval(object):
        def __init__(self, start, end):
            self.start = start
            self.end = end
    """

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []

        intervals.sort(key= lambda x:x.start)
        for inter in intervals:
            if have_a_room([inter.start,inter.end],rooms):
                continue
            rooms.append([inter.start,inter.end])
            
        return len(rooms)



def have_a_room(inter, rooms):

    for idx,room in enumerate(rooms):
        is_occupid = room[0] <= inter[0] < room[1] or room[0] <= inter[1] < room[1]
        if not is_occupid:
            rooms[idx] = [min(inter[0],room[0]), max(inter[1],room[1])]
            return True

    return False
