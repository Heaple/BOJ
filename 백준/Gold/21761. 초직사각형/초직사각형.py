import sys

input = sys.stdin.readline

N, K = map(int, input().split())
rect = list(map(int, input().split()))
li = []
abcd = {'A': [-321], 'B': [-321], 'C': [-321], 'D': [-321]}
for i in range(N):
    a, b = input().split()
    # li.append([a, int(b)])
    abcd[a].append(int(b))
abcd['A'].sort()
abcd['B'].sort()
abcd['C'].sort()
abcd['D'].sort()
# print(abcd)
for _ in range(K):
    res = [0, 0, 0]
    a, b, c, d = abcd['A'][-1], abcd['B'][-1], abcd['C'][-1], abcd['D'][-1]

    max_ = max(rect[1]*rect[2]*rect[3]*(rect[0]+a), rect[0]*rect[2]*rect[3]*(rect[1]+b), rect[1]*rect[0]*rect[3]*(rect[2]+c), rect[1]*rect[2]*rect[0]*(rect[3]+d))

    if rect[1]*rect[2]*rect[3]*(rect[0]+a) == max_:
        print('A', end=' ')
        rect[0] += abcd['A'][-1]
        print(abcd['A'].pop())
    elif rect[0]*rect[2]*rect[3]*(rect[1]+b) == max_:
        print('B', end=' ')
        rect[1] += abcd['B'][-1]
        print(abcd['B'].pop())
    elif rect[1]*rect[0]*rect[3]*(rect[2]+c) == max_:
        print('C', end=' ')
        rect[2] += abcd['C'][-1]
        print(abcd['C'].pop())
    elif rect[1]*rect[2]*rect[0]*(rect[3]+d) == max_:
        print('D', end=' ')
        rect[3] += abcd['D'][-1]
        print(abcd['D'].pop())
    # print(rect)
    # for i in li:
    #     a, b = i
    #     mul = rect[ord(a)-65]+b
    #     # print(mul)
    #     for j in range(4):
    #         if j != ord(a)-65:
    #             # print(mul)
    #             # print(rect)
    #             mul = mul*rect[j]
    #     # print(mul)
    #     if res[0] < mul:
    #         res = [mul, a, b]
    # print(res[1], res[2])
    # rect[ord(res[1])-65] += res[2]
    # li.remove([res[1], res[2]])