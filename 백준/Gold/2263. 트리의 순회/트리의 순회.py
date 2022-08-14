import sys

sys.setrecursionlimit(10**6)

n = int(input())

inorder = list(map(int, input().split()))
inorder += [0]*(100001-n)
postorder = list(map(int, input().split()))
postorder += [0]*(100001-n)
idx = [0 for _ in range(100001)]

for i in range(n):
    idx[inorder[i]] = i
# while postorder:
#     idx = inorder.index(postorder[-1])
#     postorder = inorder[:idx+1]
#     print(postorder[-1])

# idx = inorder.index(postorder[-1])
# print(idx)
# postorder = postorder[:idx+1]
# print(postorder)
# idx = inorder.index(postorder[-1])
# postorder = postorder[:idx+1]
# print(postorder)

def pre(inStart, inEnd, postStart, postEnd):
    if (inEnd < inStart or postEnd < postStart):
        return
    

    root = postorder[postEnd]
    print(root, end=' ')
    pre(inStart, idx[root]-1, postStart, postStart+(idx[root]-inStart)-1)
    pre(idx[root]+1, inEnd, postStart+idx[root]-inStart, postEnd-1)

pre(0, n-1, 0, n-1)