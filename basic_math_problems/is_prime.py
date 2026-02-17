#brute force solution
def isprime(n):
    
    flag = True
    if n<=1:
        print("Not a prime number")
        return

    for i in range(2,n):
        if n % i == 0:
            flag = False
            break
    if flag:
        print("It is a prime number")
    else:
        print("Not a prime number")
            
n = int(input())
isprime(n)

#optimal solution
def isprime(n):
    flag = True
    if n<=1:
        print("Not a prime number")
        return
    
    for i in range(2,int((n**0.5)+1)):
        
        if n%i == 0:
            flag = False
            break 
    if flag:
        print("It is a prime number")
    else:
        print("Not a prime number")
        
n = int(input())
isprime(n)

#more optimal solution
def isprime(n):
    flag = True
    if n<=1:
        print("Not a prime number")
        return
    
    if n==2:
        print("It is a prime number")
        return
    
    if n%2==0:
        print("Not a prime number")
        return
    
    
    for i in range(3,int((n**0.5)+1),2):
        
        if n%i == 0:
            flag = False
            break 
    if flag:
        print("It is a prime number")
    else:
        print("Not a prime number")
        
n = int(input())
isprime(n)
