cmd = input()
x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
count = 0

for c in cmd:
    count += 1
    if c == 'F':
        x += dxs[dir_num]
        y += dys[dir_num]
        if x == 0 and y == 0:
            break

    elif c == 'L':
        dir_num = (dir_num - 1) % 4

    elif c == 'R':
        dir_num = (dir_num + 1) % 4
    


if x != 0 and y != 0:
    print(-1)
else:
    print(count)