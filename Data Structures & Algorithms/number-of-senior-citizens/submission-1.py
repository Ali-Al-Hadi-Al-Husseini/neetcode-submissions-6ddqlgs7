class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_count = 0

        for det in details:
            age = int(det[11:13])
            if age > 60:
                senior_count += 1

        return senior_count