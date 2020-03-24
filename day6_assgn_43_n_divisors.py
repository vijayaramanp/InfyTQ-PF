
#PF-Assgn-43
def find_divisors(num):
    divisors=[]
    for i in range(1, num+1):
        if num%i==0:
            divisors.append(i)
    return len(divisors)

def find_smallest_number(num):
    for i in range(2, 1000):
        if find_divisors(i) == num:
            return i
    
num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
