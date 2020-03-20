#PF-Assgn-41
def findsum(s):
    res=0 
    for c in s:
        res=res+ int(c)
    return res
    
def find_ten_substring(num_str):
    res=[]
    for n in range(2,len(num_str)):
        for i in range (0,len(num_str)-n+1) :
           if findsum(num_str[i:i+n]) == 10:
               res.append(num_str[i:i+n])
               
    return res           
    
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
