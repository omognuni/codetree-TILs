n = int(input())

arr = []

for i in range(n):
    s = input().split()
    if len(s) >= 2:
        cmd = s[0]
        num = s[1]
    
    else:
        cmd = s[0]


    if cmd == "push_back":
        arr.append(num)
    elif cmd == "get":
        print(arr[int(num)-1])
    elif cmd == "size":
        print(len(arr))
    else:
        arr.pop()