R, C = map(int, input().split())
arr = []

for _ in range(R):
    arr.append(list(map(str, input().split())))

visited = [[0 for _ in range(R)] for _ in range(C)]

starts = [[0, 0]]

ans = 0
while starts:
    start = starts.pop()
    x = start[0]
    y = start[1]
    for i in range(x+1, R):
        for j in range(y+1, C):
            if arr[x][y] != arr[i][j] and i != R-1 and j != C-1:
                visited[i][j] = visited[x][y] + 1
                starts.append([i, j])
            
            if i == R-1 and j == C-1 and visited[x][y] == 2:
                ans += 1

print(ans)