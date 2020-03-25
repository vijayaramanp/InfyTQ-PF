#PF-Tryout
import random

def guess_number(number_in_mind):
    while True:
        x=random.randrange(1,11)
        if x == number_in_mind:
            print ('You have got it right!!!')
            break
        elif x < number_in_mind:
            print ('Number is low')           
        else:
            print ('Number is high')           

#Provide different values for number_in_mind and test your program
guess_number(4)
