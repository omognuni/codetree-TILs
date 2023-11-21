N, K = map(int ,input().split())

arr = [0 for _ in range(10001)]

for _ in range(N):
    x, score = map(str, input().split())
    x = int(x)
    if score == 'G':
        arr[x] = 1
    if score == 'H':
        arr[x] = 2


max_cnt = 0
for i in range(1, len(arr) - K + 1):
    max_cnt = max(max_cnt, sum(arr[i:i+K+1]))

print(max_cnt)