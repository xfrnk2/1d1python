from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container = defaultdict(list)
        for s in strs:
            container[''.join(sorted(s))].append(s)
        return container.values()
