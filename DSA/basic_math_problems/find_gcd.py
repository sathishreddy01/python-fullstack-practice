#Brute force approach

x,y = map(int,input().split())

answer = 0

for i in range(1,min(x,y)+1):
    
    if x % i == 0 and y % i == 0 :
        answer = i 

print(answer)

#optimal approach using euclidian algorithm 

n1 , n2 = map(int,input().split())

while(n1 > 0 and n2 > 0 ):
    
    if n1 > n2 :
        n1 = n1 % n2 
        
    else:
        n2 = n2 % n1
        
if (n1 == 0):
    print(n2)
else:
    print(n1)

#Approach3

n1 , n2 = map(int,input().split())

while(n2 != 0):

    n1 , n2 = n2 , n1 % n2

print(n1)