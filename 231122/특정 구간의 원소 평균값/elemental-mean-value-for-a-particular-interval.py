N = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(i, N):
        tmp = sum(arr[i:j+1]) / len(arr[i:j+1])
        if tmp in arr[i:j+1]:
            count += 1

print(count)