class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for i in range(3):
            char = chr(ord("a") +i)
            heapq.heappush(max_heap,(-locals()[char], char))
        
        res =["",""]
        queue = []
        while max_heap:
            freq,char = heapq.heappop(max_heap)

            while max_heap and [char,char] == res[-2:]:
                queue.append((freq,char))
                freq,char = heapq.heappop(max_heap)

            if freq >=0 or  [char,char] == res[-2:]:
                continue
            freq +=1 
            res.append(char)

            if freq < 0:
                heapq.heappush(max_heap,(freq, char))

            for item in queue:
                heapq.heappush(max_heap,item)

            queue = []

        return "".join(res)
