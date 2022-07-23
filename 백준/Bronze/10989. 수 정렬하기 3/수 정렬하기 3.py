import sys

li = [0]*10000
for i in range(int(sys.stdin.readline())):
    li[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i+1)