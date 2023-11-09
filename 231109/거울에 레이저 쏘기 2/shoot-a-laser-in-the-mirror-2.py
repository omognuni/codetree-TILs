N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))
K = int(input())

def in_range(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    return False

count = 0
dxs, dys = [1, 0 , -1 ,0], [0, 1, 0, -1]

x = 0
y = 0
dir_num = 0

if K <= N:
    dir_num = 3
    x = 0
    y = K - 1
elif K > N and K <= 2*N:
    dir_num = 2
    y = N - 1
    x = K - N - 1 
elif K > 2*N and K <= 3*N:
    dir_num = 1
    x = N - 1
    y = 3*N - K
elif K > 3*N and K <= 4*N:
    dir_num = 0
    y = 0
    x = 4*N - K

count = 0
while True:
    v = dxs[dir_num] + dys[dir_num]
    if arr[x][y] == '\\':
        v = v * -1

    if v < 0:
        dir_num = (dir_num - 1) % 4
    else:
        dir_num = (dir_num + 1) % 4

    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if not in_range(nx, ny):
        break
    
    x = nx
    y = ny
    count += 1

print(count-1)