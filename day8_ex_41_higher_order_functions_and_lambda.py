#PF-Exer-41
#This verification is based on string match.

def sum_all(function, data):
    res=0 
    for d in data:
        if function(d):
            res=res+d
    return res


list_of_nos=[100,200,300,500,1040]

greater = lambda x : x>10

divide = lambda x : x%10==0 and x<=100

range_of_values = lambda x : x>24 and x <51


#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))
