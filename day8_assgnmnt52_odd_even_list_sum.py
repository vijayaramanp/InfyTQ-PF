#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    summ=0
    if filter_func==None:
        summ=sum(list_of_num)
    elif filter_func==odd:
        odd_list=odd(list_of_num)
        summ=sum(odd_list)
        
    elif filter_func==even:
        even_list=even(list_of_num)
        summ=sum(even_list)
    
    return summ

def even(data):
    elist=[]
    for i in data:
        if i%2==0:
            elist.append(i)
    return elist

def odd(data):
    olist=[]
    for i in data:
        if i%2==1:
            olist.append(i)
    return olist

sample_data = range(1,11)

print(sum_of_numbers(sample_data,even))
