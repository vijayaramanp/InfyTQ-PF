#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func == None:
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))

def even(data):
    lis=[]
    for i in data:
        if i%2==0:
            lis.append(i)
    return lis

def odd(data):
    lis=[]
    for i in data:
        if i%2==1:
            lis.append(i)
    return lis

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))
