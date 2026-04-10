class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq_arr = [ [] for _ in range(len(nums) + 1)]

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] +=1 
        # print(freq)
        for key,value in freq.items():
            freq_arr[value].append(key)
            print(freq_arr)
        del freq 

        res = []
        # print(freq_arr)
        while len(res) < k :
            tmp = freq_arr.pop()
            while len(res) <k and len(tmp) >0 :
                res.append(tmp.pop())


        return res 

        
             


        

        

