#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    class_average=sum(list_of_marks)/10
    count_of_studs_scored_above_avg=sum(map(lambda x:x>class_average,list_of_marks))
    
    return (count_of_studs_scored_above_avg/10)*100
    
def sort_marks():
    return sorted(list_of_marks)

def generate_frequency():
    mark_frequency_list=[0]*26
    for mark in list_of_marks:
        mark_frequency_list[mark]+=1
    return mark_frequency_list
        
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
