arr = list(map(int, input().split()))

N = 6

def get_diff(i, j, k):
    total1 = arr[i] + arr[j] + arr[k]
    total2 = sum(arr) - total1
    return abs(total1-total2)


min_diff = 6 * 1e6

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)