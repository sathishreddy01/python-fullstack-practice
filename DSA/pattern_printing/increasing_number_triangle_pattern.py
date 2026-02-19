n = int(input())
temp = 1

for i in range(n):
    for j in range(i+1):
        
        print(temp,end=" ")
        temp += 1
    print()