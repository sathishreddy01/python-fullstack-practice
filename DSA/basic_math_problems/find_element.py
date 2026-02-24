x = int(input())
arr = list(map(int,input().split()))

for i in range(len(arr)):
    
    if arr[i] == x:
        print(f"Element found at {i}th position")
        break 
else:
    print("Element not found")