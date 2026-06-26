class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [num for num in nums]

        for idx in range(1,len(self.sums)):
            self.sums[idx] += self.sums[idx-1]


    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.sums[left-1] if left >0 else 0
        return self.sums[right] - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)