#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    fin=""
    lis=sentence.split()
    for i in range(0,len(lis)):
        temp=""
        if i%2==0:
            temp=lis[i]
            fin=fin+temp[::-1]+' '
        else:
            temp=lis[i]
            tem=""
            vow=""
            conso=""
            for i in temp:
                if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
                    vow=vow+i
                else:
                    conso=conso+i
            tem=conso+vow
        
            fin=fin+tem+' '
    fin=fin.strip()
    return fin

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
