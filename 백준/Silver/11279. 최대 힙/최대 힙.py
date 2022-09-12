import sys
import heapq

input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    a = int(input())

    if a == 0:
        print(-heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, -a)
    # print(heap)