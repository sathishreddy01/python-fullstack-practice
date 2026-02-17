def reverse(self, x: int) -> int:
    ans=0
    n=x
    if x<=(-2**31) or x>=(2**31-1):
        return 0
    if x<0:
        x = abs(x)
    while(x>0):
        ans = ans*10 + (x%10)
        x = x//10
    if n<0:
        return -(ans)
    else:
        return ans