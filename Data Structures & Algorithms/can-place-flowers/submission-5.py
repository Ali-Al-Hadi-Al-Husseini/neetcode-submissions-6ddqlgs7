class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_bed= [0] + flowerbed + [0]

        for i in range(1, len(new_bed) - 1):
            if new_bed[i + 1] == 0 and new_bed[i - 1] == 0 and new_bed[i] == 0  :
                new_bed[i] = 1
                n -= 1

        return n <= 0