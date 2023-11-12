a = input()
n = len(a)

count = 0
for i in range(n):
    if a[i] == '(':
        for j in range(i+1, n):
            if a[j] == ')':
                count += 1

print(count)