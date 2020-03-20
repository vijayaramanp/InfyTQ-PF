#PF-Assgn-44

def find_duplicates(list_of_numbers):
    duplicates_list=[]
    list_set=set(list_of_numbers)
    for num in list_set:
        count=list_of_numbers.count(num)
        if count>1:
            duplicates_list.append(num)
    return sorted(duplicates_list)

list_of_numbers=[12,54,68,759,24,15,12,68,987,758,25,69]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
