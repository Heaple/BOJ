import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
w = [input().rstrip() for _ in range(N)]

w.sort()
w.sort(key=lambda x: len(x))
#a = []
#s = ''
print(w[0]+'\n')
# print()
for i in range(1,len(w)):
    if w[i] != w[i-1]:
        print(w[i]+"\n")