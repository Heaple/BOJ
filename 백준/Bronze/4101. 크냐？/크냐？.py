# a = int(input())
# b = int(input())
# a, b = map(int, input().split())
# s = input()

while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    print('Yes' if b < a else 'No')