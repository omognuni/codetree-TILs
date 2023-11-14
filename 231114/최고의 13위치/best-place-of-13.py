N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

max_count = 0
for i in range(N):
    for j in range(N-2):
        count = arr[i][j:j+3].count(1)
        if count > max_count:
            max_count = count

print(max_count)