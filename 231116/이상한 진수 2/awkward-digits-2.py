a = input()

max_int = -1

for i in range(len(a)):
    new_a = ''
    if a[i] == '0':
        new_a = a[:i] + '1' + a[i+1:]
    
    if a[i] == '1':
        new_a = a[:i] + '0' + a[i+1:]
    
    if int(new_a, 2) >= max_int:
        max_int = int(new_a, 2)

print(max_int)