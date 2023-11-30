N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

numbers = [i for i in range(1, N+1)]

arrays = []

for i in range(a1-3, a1+2):
    for j in range(b1-3, b1+2):
        for k in range(c1-3, c1+2):
            if i < N and i >= -N and j < N and j >= -N and k < N and k >= -N:
                d, e, f = numbers[i], numbers[j], numbers[k]
                if [d, e, f] not in arrays:
                    arrays.append([d, e, f])
            else:
                continue


for i in range(a2-3, a2+2):
    for j in range(b2-3, b2+2):
        for k in range(c2-3, c2+2):
            if i < N and i >= -N and j < N and j >= -N and k < N and k >= -N:
                d, e, f = numbers[i], numbers[j], numbers[k]
                if [d, e, f] not in arrays:
                    arrays.append([d, e, f])
            else:
                continue

print(len(arrays))