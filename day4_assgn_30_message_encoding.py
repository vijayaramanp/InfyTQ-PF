#PF-Assgn-30

def encode(message):
    count=1
    res=''
    for i in range(0,len(message)-1):
        if message[i]==message[i+1]:
            count+=1 
        else:
            res=res+str(count)+message[i]
            count=1
    res=res+str(count)+message[-1]
    return res

#Provide different values for message and test your program
encoded_message=encode("AABBBBBC") #ABBBBCCCCCCCCAB
print(encoded_message)
