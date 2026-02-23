arr = list(map(int,input().split()))

max_element = arr[0]

index = 0

for i in range(1,len(arr)):
    
    if arr[i] >= max_element:
        max_element = arr[i]
        index = i 

print("max element: ",max_element ,"    ","index of max element: ",index)
    
    