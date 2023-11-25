N = int(input())
arr = [None for _ in range(101)]

for _ in range(N):
    x, y = map(str, input().split())
    arr[int(x)] = y

ans = []
for i in range(101):
    for j in range(i, 101):
        if arr[i] and arr[j]:
            new_arr = arr[i:j+1]
            if new_arr.count('H') == new_arr.count('G'):
                ans.append(len(new_arr) - 1)
            
            if 'G' in new_arr and 'H' not in new_arr:
                ans.append(len(new_arr) - 1)
            
            if 'H' in new_arr and 'G' not in new_arr:
                ans.append(len(new_arr) - 1)
        else:
            pass
print(max(ans))