#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    total_ticket_list=[]
    #Write your logic here
    #Write your logic here
    for t in range(1,no_of_passengers+1):
        ticket=''
        ticket=airline[0:2]+':'+source[0:3]+':'+destination[:3]+':'+str(100+t)
        total_ticket_list.append(ticket)

    if len(total_ticket_list)>5:
        ticket_number_list=total_ticket_list[-5:]
    else:
        ticket_number_list=total_ticket_list
    
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",3))
