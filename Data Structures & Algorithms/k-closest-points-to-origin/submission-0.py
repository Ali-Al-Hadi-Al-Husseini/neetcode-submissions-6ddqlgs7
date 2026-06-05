class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = -((x)**2 + (y)**2 )
            heapq.heappush(heap,(distance,(x,y)))
            if len(heap) > k :
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
