class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m 
        for num in nums2:
            nums1[idx] = num
            idx += 1


        nums1.sort()
        return nums1 