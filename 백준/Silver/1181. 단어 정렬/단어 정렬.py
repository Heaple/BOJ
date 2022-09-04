import sys

input = sys.stdin.readline

N = int(input())
w = [input().rstrip() for _ in range(N)]

w.sort()
w.sort(key=lambda x: len(x))
a = []
for i in w:
    if i not in a:
        print(i)
        a.append(i)