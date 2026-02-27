
def rev_array(arr, start, end):
    
    if start < end:
        
        arr[start], arr[end] = arr[end], arr[start]
        
        return rev_array(arr, start + 1, end - 1)
    
    return arr
    
arr = list(map(int,input().split()))
start = 0
end = len(arr) - 1
print(rev_array(arr, start, end))