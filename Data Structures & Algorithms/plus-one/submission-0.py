class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) -1 

        while idx >= 0 :
            if digits[idx] < 9 :
                digits[idx] += 1
                return digits 
            else:
                digits[idx] = 0
                idx -= 1 

        digits.insert(0,1)

        return digits 