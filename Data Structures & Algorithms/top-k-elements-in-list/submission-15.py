class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count fre
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # list of list of nums on certain fre index
        # take 1 more becasue all the elements can be same number
        fr = [[] for i in range(len(nums) + 1)]
        for num, fre in count.items():
            fr[fre].append(num)

        # traverse list from last adding numbers on certain fre
        # for each i in len(fre)
        # for each num in fre[i]
        #append num and return
        res = []
        for i in range(len(fr) - 1, 0, -1):
            for num in fr[i]:
                res.append(num)
                if len(res) == k:
                    return res