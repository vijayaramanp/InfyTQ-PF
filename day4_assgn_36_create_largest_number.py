#PF-Assgn-36
def create_largest_number(number_list):
    num=''
    for no in number_list:
        maxx=max(number_list)
        num=num+str(maxx)
        number_list.remove(maxx)
    num=num+str(number_list[0])
    return int(num)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
