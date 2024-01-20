n, m = map(int, input().split())

MAX = 10**9

for i in range(1, MAX):
    if i % n == 0 and i % m == 0:
        print(i)
        break