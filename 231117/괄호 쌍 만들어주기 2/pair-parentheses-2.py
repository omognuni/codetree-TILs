data = input()

count = 0
for i in range(len(data)-1):
    if data[i] == '(' and data[i+1] == '(':
        for j in range(i+2, len(data)-1):
            if data[j] == ')' and data[j+1] == ')':
                count += 1       
                
print(count)