class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_freq = sorted(Counter(tasks).values())
        curr_start = 0
        cycles = 0 

        for i in range(len(tasks_freq)-1, -1, -1):
            curr_end = curr_start  + tasks_freq[i] + ((tasks_freq[i]-1 ) * n) 
            cycles = max(cycles, curr_end)
            curr_start += 1 

        return max(cycles,len(tasks))