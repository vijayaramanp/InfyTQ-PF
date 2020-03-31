#PF-Assgn-50
def sms_encoding(data):
    words=data.split()
    final=''
    for word in words:
        if len(word)>1:
            temp=''
            for char in word:
                if char!='a' and char!='e' and char!='i' and char != 'o' and char!='u' and char!='A' and char!='E' and char!='I' and char!='O' and char!='U':
                    temp=temp+char
            final=final+temp+' '
        else:
            final+=word+' '
    return final.strip()
    
data="I love Python"
print(sms_encoding(data))
