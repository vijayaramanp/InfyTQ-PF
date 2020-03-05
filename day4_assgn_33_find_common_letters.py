#PF-Assgn-33
#Solution 1
def find_common_characters(msg1,msg2):
    res=''
    for char in msg1:
        if char in msg2 and char!=' ' and char not in res:
                res=res+char
    if res=='':
        return -1
    else:
        
        return res
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)


'''
#Solution 2
def find_common_characters(msg1,msg2):
    res=''
    for char in msg1:
        if char in msg2 and char!=' ':
            res=res+char
    if res=='':
        return -1
    else:
        x=''.join(sorted(set(res),key=res.index))
        return x
        
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
'''
'''
#Solution 3
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
'''

'''
#Solution 4
# This solution passess
5 out of 6 test cases passed.

1 out of 1 structural test cases passed.

4 out of 5 logical test cases passed



#PF-Assgn-33

def find_common_characters(msg1,msg2):
    res=''
    for char in msg1:
        if char in msg2 and char!=' ':
            res=res+char
    if res=='':
        return -1
    else:
        return res
        
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)

'''
#Solution 5: 50% of the test cases passes
'''

#PF-Assgn-33

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
#solution 6
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

