def sumof_numbers(n):
    
    if n <= 0:
        return
    if n == 1:
        return 1
    return n + sumof_numbers(n-1)
    
n= int(input())
total_sum = 0
print(sumof_numbers(n))