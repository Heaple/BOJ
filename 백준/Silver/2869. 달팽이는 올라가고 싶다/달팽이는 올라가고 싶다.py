from math import ceil


A, B, V = map(int, input().split())
day = 0
night = False
now = 0
print(ceil((V-B)/(A-B)))