def is_palindrome(string,start,end):
    
    if start < end: 
        
        if string[start] != string[end]:
            return "Not a palindrome"
            
        return is_palindrome(string, start + 1, end - 1)
    
    return "It is a palindrome"


string = input().strip().lower()
print(is_palindrome(string,0,len(string) - 1))