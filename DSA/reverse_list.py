def rev(arr,i,n):
    if (i is None) or (i >= (n/2)):
        return
    else:
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp
        rev(arr,i + 1,n)

li=[1, 2, 3, 4, 5]
rev(li, 0, 5)
print(li)

def palindrome(string,i,n):
    if(i >= (n/2)):
        return True
    if(string[i] != string[n-i-1]):
        return False
    return palindrome(string, i + 1, n)

s = "malayalam"
if palindrome(s, 0, len(s)):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")