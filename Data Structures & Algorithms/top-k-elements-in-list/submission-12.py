class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequesncies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # add (fre, num) in a heap, keep the hight at k 
        heap = []
        for num, fre in count.items():
            heapq.heappush(heap, [fre, num])
            if len(heap) > k:
                heapq.heappop(heap)

        # add in res from heap and return 
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

