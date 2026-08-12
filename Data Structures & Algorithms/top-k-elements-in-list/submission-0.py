class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        #dictionary of num and count
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # frequency first list of list(c, num)
        freq = []
        for num, c in count.items():
            freq.append([c, num])
        freq.sort()

        res = []
        # while len(res) < k append pop freq 1s index of each list
        while len(res) < k:
           res.append(freq.pop()[1])

        return res

