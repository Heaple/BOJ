a = list(map(int, input().split()))
res = 0
if a.count(a[0]) == 2:
    res += 1000+(a[0]*100)
elif a.count(a[1]) == 2:
    res += 1000+(a[1]*100)
elif a.count(a[1]) == 3:
    res += 10000+(a[0]*1000)
else:
    res += max(a)*100

print(res)