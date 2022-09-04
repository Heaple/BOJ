N = int(input())
w = [input() for _ in range(N)]

w.sort()
w.sort(key=lambda x: len(x))
a = []
for i in w:
    if i not in a:
        print(i)
        a.append(i)