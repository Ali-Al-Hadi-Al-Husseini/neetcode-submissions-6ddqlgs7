from _heapq import heappush
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap,num)
        else:
            heapq.heappush(self.max_heap,-1 * num)

        if len(self.max_heap) > len(self.min_heap) :
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-1 * val)
        elif  len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-1 * val)
        self.length += 1
        

    def findMedian(self) -> float:
        if self.length % 2 == 0 :
            return (self.min_heap[0] + (self.max_heap[0] * -1)) / 2 
        if len(self.min_heap) >= len(self.max_heap):
            return self.min_heap[0]
        
        return self.max_heap[0] * -1
        

        