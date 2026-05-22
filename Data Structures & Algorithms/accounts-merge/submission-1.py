class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = {}

        for account in accounts:
            for eml in account[1:]:
                if eml not in adj_list:
                    adj_list[eml] = {"emails":[],"name":account[:1][0]}
                adj_list[eml]["emails"].extend(account[1:])

        def get_children(eml,visited):
            queue = deque()
            queue.append(eml)
            children = []

            while queue:
                curr_eml = queue.popleft()
                if curr_eml in visited:
                    continue
                visited.add(curr_eml)
                children.append(curr_eml)

                for child in adj_list[curr_eml]["emails"]:
                    if child not in visited:
                        queue.append(child)

            return children


        visited_eml = set()
        result = defaultdict(list)
        for eml in adj_list.keys():
            if eml in visited_eml:
                continue
            emls = get_children(eml,visited_eml)
            result[adj_list[eml]['name']].append(emls)
        
        res = []

        for name in result.keys():
            for emails in result[name]:
                res.append([name] + emails)

        return res 

        