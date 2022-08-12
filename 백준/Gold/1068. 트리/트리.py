N = int(input())
node = list(map(int, input().split()))
A = int(input())

stack = [A]
node[A] = -2

while stack:
    a = stack.pop()
    for i in range(node.count(a)):
        stack.append(node.index(a))
        node[stack[-1]] = -2
res = 0

for i in range(N):
    if node[i] != -2 and node[i] != -1 and node.count(i) == 0:
        res += 1

if len(node) == 2:
    print(1)
    quit()

print(res)