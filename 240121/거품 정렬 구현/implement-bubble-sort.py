n = int(input())
arr = list(map(int, input().split()))

is_sorted=False

while not is_sorted:
    is_sorted = True
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                is_sorted = False

            
print(" ".join([str(i) for i in arr]))