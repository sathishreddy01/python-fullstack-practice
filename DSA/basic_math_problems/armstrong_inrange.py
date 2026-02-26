def is_armstrong(n):
    
    temp = n
    answer = 0
    no_of_digits = 0
    
    while(n>0):
        
        no_of_digits += 1
        n = n // 10
        
    n = temp
    
    while(n>0):
        
        rem = n%10
        answer += (rem ** no_of_digits)
        n = n // 10
    
    if answer == temp:
        return True
    else:
        return False



x , y = map(int,input().split())

for i in range(x,y+1):
    
    if is_armstrong(i):
        print(i,end=" ")