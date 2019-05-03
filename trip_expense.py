#PF-Assgn-3
#This verification is based on string match.

mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five=False


per_head_cost=(((distance_one_way*2)/mileage)*amount_per_litre)/4

if per_head_cost%5==0:
    divisible_by_five=True


print(per_head_cost)
print(divisible_by_five)
