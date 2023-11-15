R, C = map(int, input().split())
arr = []

for _ in range(R):
    arr.append(list(map(str, input().split())))


suc = 0

for i in range(R-1):
    for j in range(C-1):
        count = 0
        for k in range(i+1, R):
            for l in range(j+1, C):
                if arr[i][j] != arr[k][l]:
                    count += 1

        if count == 2:
            suc += 1

print(suc)