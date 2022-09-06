from collections import deque
import sys


input = sys.stdin.readline

N = int(input())
deq = deque()

for i in range(N):
    inp = input().split()

    if inp[0] == 'push_back':
        deq.append(inp[1])
    elif inp[0] == 'push_front':
        deq.appendleft(inp[1])
    elif inp[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif inp[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    elif inp[0] == 'size':
        print(len(deq))
    elif inp[0] == 'empty':
        print(0 if deq else 1)
    elif inp[0] == 'front':
        print(deq[0] if deq else -1)
    elif inp[0] == 'back':
        print(deq[-1] if deq else -1)