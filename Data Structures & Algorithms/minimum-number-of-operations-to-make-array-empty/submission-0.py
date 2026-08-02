class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        numbers = set(nums)
        operations = 0

        for num in numbers:
            if count[num] == 1 :
                return -1 
            operations += get_operations_count(num,count)

        return operations
            

def get_operations_count(curr_num,counter):
    operations = 0
    if counter[curr_num] % 3 == 0 :
        return counter[curr_num] // 3 
    else:
        return counter[curr_num] // 3  + 1 

    # return (counter[curr_num] // 3 ) 
