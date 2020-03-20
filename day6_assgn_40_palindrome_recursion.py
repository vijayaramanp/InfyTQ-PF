#PF-Assgn-40
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[len(word) - 1]:
        return is_palindrome(word[1:len(word)-1])
    else:
        return False

#Provide different values for word and test your program
result=is_palindrome("madam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
