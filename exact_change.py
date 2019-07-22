#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    flag=0

    #Start writing your code here
    if ((no_of_five*5)+no_of_one)>=rupees_to_make:
        fives=rupees_to_make//5
        ones=rupees_to_make%5
        if fives<=no_of_five and ones<=no_of_one:
            five_needed=fives
            one_needed=ones
            flag=1
        elif fives>no_of_five:
            five_needed=no_of_five
            one_needed=rupees_to_make-(five_needed*5)
            if one_needed<=no_of_one:
                flag=1
            
                
            
        


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    if flag==1:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,4,10)
