
#PF-Exer-34
import math

def find_number_of_combination(number_of_flavours):
    total_combination=0
    n=number_of_flavours
    x=math.factorial(n)
    for r in range(number_of_flavours+1):
        y=math.factorial(r)
        z=math.factorial(n-r)
        c=x/(y*z)
        total_combination+=c
    
    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)
