#PF-Assgn-36
def create_largest_number(number_list):
    num=''
    number_list.sort(reverse=True)
    for no in number_list:
        num=num+str(no)
    return int(num)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
