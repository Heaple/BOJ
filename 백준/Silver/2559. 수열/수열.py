N, K = map(int, input().split())
temperatures = list(map(int, input().split()))
for i in range(1, N):
    temperatures[i] += temperatures[i-1]

temperatures.insert(0, 0)

res = []

for i in range(K, N+1):
    res.append(temperatures[i]-temperatures[i-K])

print(max(res))