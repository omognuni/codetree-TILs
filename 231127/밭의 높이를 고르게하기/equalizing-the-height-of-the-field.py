import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(N - T + 1):
    cost = 0
    new_arr = arr[i:i+T]
    for j in new_arr:
        cost += int(abs(j-H))
    
    min_val = min(cost, min_val)

print(min_val)