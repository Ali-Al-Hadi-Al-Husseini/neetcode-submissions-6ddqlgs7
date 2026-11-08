class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int) :
        people_that_know = set()
        visited= set()
        adj_list = defaultdict(list)

        for a,b,t in meetings:
            adj_list[a].append((b,t))
            adj_list[b].append((a,t))
        

        queue = deque()
        queue.append((firstPerson,0))
        queue.append((0,0))


        while queue:
            curr,curr_time = queue.popleft()
            if (curr,curr_time) in visited:
                continue
            visited.add((curr,curr_time) )
            people_that_know.add(curr)


            for person ,time in adj_list[curr]:
                if curr_time > time :
                    continue
                queue.append((person,time))



        return list(people_that_know) 
