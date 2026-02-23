#approach 1

def primeInRange(x):
    
    if x<=1 :
        return
    
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return 
        
    print(x,end=" ")

n = int(input())
m = int(input())

for i in range(n,m+1):
    primeInRange(i)


#Approach 2 (skip evens approach)


def primeInRange(x):
    
    if x <= 1:
        return
    
    if x == 2:
        print(x,end=" ")
        return
    
    if x % 2 == 0:
        return
    
    for i in range(3,int(x**0.5)+1):
        
        if x % i == 0:
            return
        
    print(x,end=" ")

n = int(input())
m = int(input())

for i in range(n,m+1):
    primeInRange(i)

