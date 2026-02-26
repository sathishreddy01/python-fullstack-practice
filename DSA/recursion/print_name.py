def print_name(n):
    
    if n <= 0 :
        return
    
    print("Ashish", end=" ")
    
    print_name(n - 1)
    
n = int(input())

print_name(n)