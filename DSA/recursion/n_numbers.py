def n_numbers(n):
    
    if n <= 0 :
        return
    
    n_numbers(n-1)
    
    print(n,end=" ")

n = int(input())

n_numbers(n)