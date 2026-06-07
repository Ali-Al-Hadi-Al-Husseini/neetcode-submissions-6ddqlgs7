class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [1,1,1]

        for trip in triplets:
            if not all([trip[i] <= target[i] for i in range(3)]):
                continue
            if any(([trip[i] == target[i] for i in range(3)])):
                curr = [max(curr[0],trip[0]), max(curr[1],trip[1]), max(curr[2],trip[2])]
                if curr ==  target:
                    return True

        return False
