n = int(input())
string = input()

count = 0
for i in range(n-2):
    if string[i] == 'C':
        for j in range(i+1, n - 1):
            if string[j] == 'O':
                for k in range(j+1 , n):
                    if string[k] == 'W':
                        count += 1

print(count)