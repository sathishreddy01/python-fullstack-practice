n = int(input())

for i in range(n):
    
    asciivalue=65
    for j in range(i+1):
        print(chr(asciivalue),end=" ")
        asciivalue += 1
        
    print()