n, m = map(int, input().split())
arr = [[0 for _ in range(n+1)] for __ in range(n+1)]
dxs, dys = [0, -1, 0 , 1], [1, 0 ,-1 ,0]

def in_range(x, y):
    if x >= 0  and x < n and y >= 0 and y < n:
        return True
    return False

for i in range(m):
    r, c = map(int, input().split())
    
    count = 0
    arr[r-1][c-1] = 1

    for j in range(4):
        nx = r - 1 + dxs[j]
        ny = c - 1 + dys[j]

        if in_range(nx, ny) and arr[nx][ny] == 1:
            count += 1

    if count == 3:
        print(1)
    else:
        print(0)