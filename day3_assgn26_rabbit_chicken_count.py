#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if legs%2!=0 or heads==0 or heads>legs:
        print(error_msg)
    else:
        rabbit_count=int((legs-(2*heads))/2)
        chicken_count=int(heads-rabbit_count)
        print(chicken_count,rabbit_count)

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
#Provide different values for heads and legs and test your program
solve(35,94)

