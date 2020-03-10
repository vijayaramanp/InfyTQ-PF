#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count_of_pairs=0
    for i in range(0,len(num_list)-1):
        for j in range(i+1,len(num_list)):
            if num_list[i]+num_list[j]==n:
                count_of_pairs+=1 
                break
    return count_of_pairs

num_list=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print(find_pairs_of_numbers(num_list,n))
