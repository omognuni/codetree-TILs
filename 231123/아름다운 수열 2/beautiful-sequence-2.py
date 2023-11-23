# from copy import deepcopy
N, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(N-M+1):
    new_arr = a[i:i+M]
    b_visited = [False for _ in range(M)]

    for j in range(M):
        for k in range(M):
            if b[k] == new_arr[j] and not b_visited[k]:
                b_visited[k]=True

    if False not in b_visited:
        count+=1

print(count)