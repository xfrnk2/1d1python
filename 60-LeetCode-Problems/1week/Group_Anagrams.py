from collections import defaultdict
from typing import DefaultDict, List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container: DefaultDict = defaultdict(list)
        for s in strs:
            container[''.join(sorted(s))].append(s)
        return list(container.values())
