class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            result.setdefault(sortedS, []).append(s)
        return list(result.values())

