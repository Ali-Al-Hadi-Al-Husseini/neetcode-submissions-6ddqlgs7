class Solution:
    def candy(self, ratings: List[int]) -> int:
        childs = len(ratings)
        candies = [1] * childs

        for idx in range(1,childs):
            if ratings[idx -1 ] > ratings[idx]:
                candies[idx-1] = candies[idx] +1
            elif ratings[idx] > ratings[idx - 1]:
                candies[idx] = candies[idx-1] +1
        print(candies)

        for idx in range(childs-1,0,-1):

            if ratings[idx -1 ] > ratings[idx]:
                candies[idx-1] = max(candies[idx] +1,candies[idx-1])
            elif ratings[idx] > ratings[idx - 1] :
                candies[idx] = max(candies[idx-1] +1,candies[idx])




        print(candies)
        return sum(candies)