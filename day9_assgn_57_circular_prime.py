#PF-Assgn-57
import math
def check_prime(number):
    if number==1:
        return True
    else:
        end_limit=int(math.sqrt(number))+1
        for i in range(2, end_limit):
            if number%i==0:
                return False
    return True

def rotations(num):
    rotations=[]
    rotations.append(num)
    str_num=str(num)
    lenght=len(str_num)-1
    temp=str_num
    while lenght:
        temp=temp[1:]+temp[0:1]
        rotations.append(int(temp))
        lenght -= 1
    return rotations

def get_circular_prime_count(limit):
    circular_prime=[]
    for i in range(2, limit):
        flag=1
        rotations_list=rotations(i)
        for num in rotations_list:
            if check_prime(num) == False:
                flag=0
                break
        if flag:
            circular_prime.append(i)
    return len(circular_prime)

#Provide different values for limit and test your program
print(get_circular_prime_count(100))
