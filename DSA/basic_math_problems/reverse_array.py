#Brute force approach
arr = list(map(int,input().split()))

for i in range(len(arr)-1,-1,-1):
    
    print(arr[i], end=" ")


#Approach2 (inplace replacement)
arr = list(map(int,input().split()))

first = 0
last = len(arr)-1

while(first <= last):
   
    arr[first] , arr[last] = arr[last] , arr[first]
    
    first += 1 
    last -= 1 
    
for i in range(len(arr)): 
    print(arr[i],end=" ")
    
    
    
