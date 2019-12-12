#PF-Assgn-33

def find_common_characters(msg1,msg2):
    temp=""
    for a in msg1:
        if a!=' ':
            for b in msg2:
                if a==b:
                    temp=temp+a
    x=''.join(sorted(set(temp),key=temp.index))
    if x=='':
        return -1
    else:
        return x
    

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
