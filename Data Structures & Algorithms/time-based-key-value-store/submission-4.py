class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        stamps = self.time_map[key]
        if stamps[0][1] > timestamp:
            return ""

        left,right = 0 , len(stamps) -1 
        while left <= right:
            mid = (left + right) // 2

            if stamps[mid][1] == timestamp:
                return stamps[mid][0]

            elif stamps[mid][1] > timestamp:
                right = mid - 1

            else:
                left = mid + 1 
        return stamps[right][0]


