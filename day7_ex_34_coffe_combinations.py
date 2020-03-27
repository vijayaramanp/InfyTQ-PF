
#PF-Exer-34
import math

def find_number_of_combination(number_of_flavours):
    total_combination=0
    n=number_of_flavours
    for r in range(number_of_flavours+1):
        x=math.factorial(n)
        y=math.factorial(r)
        z=math.factorial(n-r)
        c=x/(y*z)
        total_combination+=c
    
    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)

'''
#PF-Exer-34
import math
def find_number_of_combination(number_of_flavours):
    total_combination=0
    if number_of_flavours == 0:
        total_combination = 1 
    else:
        total_combination = math.factorial(number_of_flavours) + 1
    
    return total_combination

#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(4)
print(number_of_combination)
'''
