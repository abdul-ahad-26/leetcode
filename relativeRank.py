class Solution:
    def findRelativeRanks(self, score):
        sorted_scores = sorted(score, reverse=True)

        rank_map = {}
        for i, val in enumerate(sorted_scores):
            if i == 0:
                rank_map[val] = "Gold Medal"
            elif i == 1:
                rank_map[val] = "Silver Medal"
            elif i == 2:
                rank_map[val] = "Bronze Medal"
            else:
                rank_map[val] = str(i + 1)

        result = []
        for s in score:
            result.append(rank_map.get(s))

        return result


score = [10,3,8,9,4]

s1 = Solution()
print(s1.findRelativeRanks(score))
