import sys
n = int(input())

arr = list(map(int, input().split()))

sum_min = sys.maxsize

for i in range(n):
    total = 0
    for j in range(n):
        dist = abs(i-j)
        total += dist*arr[j]
    
    if total < sum_min:
        sum_min = total

print(sum_min)