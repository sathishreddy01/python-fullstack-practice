def isPalindrome(n):
    if n<0:
        return "false"
    temp = n
    ans = 0

    while(n>0):
    
        ans = ans*10 + (n%10)
        n=n//10

    if temp == ans:
        return "true"
    else:
        return "false"
n= int(input())
print(isPalindrome(n))