class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)

        fr = [[] for i in range(len(nums)+1)]

        for key, val in count.items():
            fr[val].append(key)

        res = []
        for i in range(len(fr)-1, 0, -1):
            for n in fr[i]:
                res.append(n)
                if len(res) == k:
                    return res

