n = int(input())
arr = list(map(int, input().split()))

max_sum = -1
for i in range(n - 2):
    for j in range(i + 2, n):
        tmp = arr[i] + arr[j]
        max_sum = max(tmp, max_sum)

print(max_sum)