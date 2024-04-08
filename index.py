import heapq
H=[4,7,8,11,5,9]
heapq.heapify(H)
#adding element
heapq.heappush(H,10)
heapq.heappush(H,9)
heapq.heappush(H,13)
print(H)
#removing
heapq.heappop(H)
print(H)
heap=[3,5,6,7,23,5]
heapq.heapify(heap)
heapq.heappop(heap)
print(heap)