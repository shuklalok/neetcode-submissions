class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26
            for t in s:
                count[ord(t) - ord('a')] += 1
            res.setdefault(tuple(count), []).append(s)
        return list(res.values())


