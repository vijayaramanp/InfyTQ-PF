#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    for i in name_list:
        if len(i)>2 and i.endswith('at'):
            count1+=1
        if i.count('at'):
            count2+=1
            
    print("_at -> ",count1)
    print("%at% -> ",count2)

#Provide different names in the list and test your program
name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)
