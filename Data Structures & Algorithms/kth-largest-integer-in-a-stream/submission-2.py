import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        #include given set into heap aka list
        for i in nums:
            self.heap.append(i)
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        #modify heap by including an element
        heapq.heappush(self.heap, val)

        #ensure we stay at a max k elements such that the min is at the root
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]