import heapq
import sys

input = sys.stdin.readline

heap = []

N = int(input().rstrip())

for i in range(N):
    a = int(input().rstrip())

    if a == 0:
        print(heapq.heappop(heap) if heap else 0)
        continue

    heapq.heappush(heap, a)