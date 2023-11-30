N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

numbers = [i for i in range(1, N+1)]

arrays = []

for i in range(a1-2, a1+3):
    for j in range(b1-2, b1+3):
        for k in range(c1-2, c1+3):
            if i <= 0 or j <= 0 or k <= 0:
                continue
            elif i not in numbers or j not in numbers or k not in numbers:
                continue
            elif [i, j, k] not in arrays:
                arrays.append([i, j, k])


for i in range(a2-2, a2+3):
    for j in range(b2-2, b2+3):
        for k in range(c2-2, c2+3):
            if i <= 0 or j <= 0 or k <= 0:
                continue
            elif i not in numbers or j not in numbers or k not in numbers:
                continue
            elif [i, j, k] not in arrays:
                arrays.append([i, j, k])

print(len(arrays))