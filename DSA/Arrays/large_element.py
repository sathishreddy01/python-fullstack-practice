arr = list(map(int,input().split()))

ans = arr[0]

for i in range(len(arr)):
    
    if arr[i] > ans :
        
        ans = arr [i]

print(ans)