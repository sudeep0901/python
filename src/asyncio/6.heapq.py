import heapq

lst = [0, 3, 99, 4, 3, 5, 6, 0]

def heapsort(lst):
    h = []
    for value in lst:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


result = heapsort(lst)
print(result)

h = []

heapq.heappush(h, (100, "Sudeep Patel"))
heapq.heappush(h, (10, "Manasvi Patel"))
heapq.heappush(h, (5, "Om"))

popped = heapq.heappop(h)
print(popped)