#PF-Assgn-31
def check_palindrome(word):
    temp=word[::-1]
    if word==temp:
        return True
    else:
        return False

status=check_palindrome("MAN")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
