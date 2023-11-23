N, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


count = 0
for i in range(N-M+1):
    new_arr = a[i:i+M]
    flag = True
    for j in range(M):
        if not b[j] in new_arr:
            flag = False
            break
    if flag:
        count+=1

print(count)