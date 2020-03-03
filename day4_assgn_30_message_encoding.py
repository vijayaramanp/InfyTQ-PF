#PF-Assgn-30

def encode(message):
    count=1
    res=''
    for i in range(0,len(message)-1):
        current_char=message[i]
        next_char=message[i+1]
        if current_char==next_char:
            count+=1 
        else:
            res=res+str(count)+current_char
            count=1
    res=res+str(count)+message[-1]
    return res

#Provide different values for message and test your program
encoded_message=encode("AABBBBBC") #ABBBBCCCCCCCCAB
print(encoded_message)
