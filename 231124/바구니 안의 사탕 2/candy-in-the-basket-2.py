N, K = map(int, input().split())
arr = [0 for _ in range(401)]


for _ in range(N):
    x, y = map(int, input().split())
    arr[y] += x

max_val = 0
for c in range(K, 200):
    max_val = max(sum(arr[c-K:c+K+1]), max_val)

print(max_val)