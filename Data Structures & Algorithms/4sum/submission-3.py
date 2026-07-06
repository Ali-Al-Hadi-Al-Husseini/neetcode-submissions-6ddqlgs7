class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()


        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                pairs.append((nums[i] + nums[j], i, j))
        pairs.sort()

        res = set()
        m = len(pairs)
        lo, hi = 0, m - 1

        while lo <= hi:
            s = pairs[lo][0] + pairs[hi][0]
            if s == target:
                left_val = pairs[lo][0]
                l_end = lo
                while l_end < m and pairs[l_end][0] == left_val:
                    l_end += 1

                right_val = pairs[hi][0]
                r_start = hi
                while r_start >= 0 and pairs[r_start][0] == right_val:
                    r_start -= 1
                r_start += 1

                for a in range(lo, l_end):
                    _, i1, j1 = pairs[a]
                    for b in range(max(a, r_start), hi + 1) if left_val == right_val else range(r_start, hi + 1):
                        _, i2, j2 = pairs[b]
                        idxs = {i1, j1, i2, j2}
                        if len(idxs) == 4:
                            quad = tuple(sorted((nums[i1], nums[j1], nums[i2], nums[j2])))
                            res.add(quad)

                lo = l_end
                hi = r_start - 1
            elif s < target:
                lo += 1
            else:
                hi -= 1

        return [list(q) for q in res]