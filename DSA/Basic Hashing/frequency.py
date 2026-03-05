
#using conditional statements

arr = list(map(int,input().split()))

freq = {}

for num in arr:
    
    if num in freq:
        
        freq[num] += 1
    
    else:
    
        freq[num] = 1
    
print(freq)


#using get function

arr = list(map(int,input().split()))

freq = {}

for num in arr:
    
    freq[num] = freq.get(num,0) + 1
    
print(freq)