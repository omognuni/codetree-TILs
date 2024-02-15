k = int(input())
arr = list(map(int, input().split()))

for i, x in enumerate(arr):
    min = i
    for j in range(i+1, k):
        if arr[min] > arr[j]:
            min = j
    tmp = arr[i]
    arr[i] = arr[min]
    arr[min] = tmp

print(" ".join([str(a) for a in arr]))