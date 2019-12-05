#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    ticket_cost=37550.0
    total_ticket_cost=(ticket_cost*no_of_adults)+((ticket_cost/3)*no_of_children)
    total_ticket_cost=total_ticket_cost+(total_ticket_cost*7/100)
    total_ticket_cost=total_ticket_cost-(total_ticket_cost*10/100)

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)
