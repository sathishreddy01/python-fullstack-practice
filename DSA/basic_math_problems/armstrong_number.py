n = int(input())

noofdigits = 0 

temp = n

answer = 0

while(temp > 0):
    
    noofdigits += 1 
    
    temp = temp // 10
    
temp = n

while(temp>0):
    
    rem = temp % 10 
    
    answer += (rem**noofdigits)
    
    temp //= 10
    
if n == answer :
    print("It is a armstrong number")

else:
    print("Not a armstrong number")

