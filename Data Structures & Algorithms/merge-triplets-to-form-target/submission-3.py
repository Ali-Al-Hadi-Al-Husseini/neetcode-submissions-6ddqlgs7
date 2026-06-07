class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets[0])
        curr = [1] * n

        for trip in triplets:
            if not all([trip[i] <= target[i] for i in range(n)]):
                continue
            if any(([trip[i] == target[i] for i in range(n)])):
                curr = [max(curr[i],trip[i]) for i in range(n)]
                if curr ==  target:
                    return True

        return False
