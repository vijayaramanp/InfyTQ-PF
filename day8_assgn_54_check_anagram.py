

#PF-Assgn-54
def check_anagram(data1,data2):
    if len(data1)!=len(data2):
        return False
    for i in range(0,len(data1)):
        if data1[i]==data2[i]:
            return False
        if data1.count(data1[i])!=data2.count(data1[i]):
            return False
    return True

print(check_anagram("eat","tea"))
