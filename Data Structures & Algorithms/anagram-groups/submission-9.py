class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            res.setdefault(sortedS,[]).append(s)
        return list(res.values())


