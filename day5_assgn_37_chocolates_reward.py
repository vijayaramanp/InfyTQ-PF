#PF-Assgn-37

#Global variables
child_id=(101, 201, 301, 401, 501)
chocolates_received=[10, 5, 3, 2, 4]

def calculate_total_chocolates():
    return sum(chocolates_received)

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates>0:
        if child_id_rewarded in child_id:
            child_id_index=child_id.index(child_id_rewarded)
            chocolates_received[child_id_index]+=extra_chocolates
            print(chocolates_received)
        else:
            print("Child id is invalid")
    else:
        print("Extra chocolates is less than 1")    

print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(201,2)

