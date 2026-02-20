n = int(input())

asciivalue = 65 + n - 1

for i in range(n):
    
    for j in range(i+1):
        
        print(chr(asciivalue+j),end=" ")
    
    asciivalue -= 1
    print()
    

