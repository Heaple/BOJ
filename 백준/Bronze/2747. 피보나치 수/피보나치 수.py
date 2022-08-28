dp = [-1]*10000
dp[0] = 0
dp[1] = 1
N = int(input())
def fib(N):
    if N < 2:
        return N
    if dp[N] == -1:
        dp[N] = fib(N-1)+fib(N-2)
    
    return dp[N]

print(fib(N))