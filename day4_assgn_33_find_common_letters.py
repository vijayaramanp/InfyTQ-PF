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

#Solution 2: 50% of the test cases passes
'''#PF-Assgn-33

def find_common_characters(msg1,msg2):
    res=""
    temp=list(sorted(set(msg1)&set(msg2)))
    for char in temp:
        if char!=' ':
            res=res+char
    if res==' ':
        return -1
    else:
        res=res
        return res

#Provide different values for msg1,msg2 and test your program
msg1="Python"
msg2="python"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
'''
#solution 3
'''
#PF-Assgn-33
def find_common_characters(msg1,msg2):
    res=""
    x=set(msg1)&set(msg2)
    for char in x:
        if char!=' ':
            res=res+char
    temp=''.join(sorted(set(res),key=res.index))
    if temp==' ':
        return -1
    else:
        temp=temp
        return temp
#Provide different values for msg1,msg2 and test your program
msg1="Python"
msg2="python"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)

'''

