from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = defaultdict(int)
        for i in nums:
            groups[i] += 1
        return sorted(groups, key = groups.get, reverse = True)[:k]