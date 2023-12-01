n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr = [str(i) for i in arr]
print(" ".join(arr))
print(" ".join(list(reversed(arr))))