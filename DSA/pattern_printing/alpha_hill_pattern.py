n = int(input())

for i in range(n):
    
    asciivalue=65
    for j in range(n-(i+1),0,-1):
        print(" ",end=" ")
        
    breakpoint = ((2*i)+1)//2
    
    for j in range((2*i)+1):
        
        
        if j < breakpoint:
            print(chr(asciivalue),end=" ")
            asciivalue += 1 
            
        elif j == breakpoint:
            print(chr(asciivalue),end=" ")
        
        else:
            asciivalue -= 1 
            print(chr(asciivalue),end=" ")
    
    
    print()