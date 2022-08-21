import sys

input = sys.stdin.readline

a = []

for i in range(3):
    a.append(int(input()))

b = []

for i in range(2):
    b.append(int(input()))

print(min(a)+min(b)-50)