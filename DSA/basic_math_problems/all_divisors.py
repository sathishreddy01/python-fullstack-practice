#Brute force approach 
n = int(input())

for i in range(1,n+1):
    
    if n % i == 0:
        
        print(i,end=" ")

#Optimal approach
n = int(input())
res = []

if n>0:
    for i in range(1,int(n**0.5)+1):
    
        if n % i == 0:
        
            res.append(i)
        
            if i != (n//i):
                res.append(n//i)
            
    res = sorted(res)
    print(res)
    
else:
    print("No divisors")
        
        