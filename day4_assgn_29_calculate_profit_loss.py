#PF-Assgn-29
def calculate(distance,no_of_passengers):
    fuel_price_per_litre=70
    milege_per_litre=10
    ticket_price=80
    expenditure=(distance/milege_per_litre)*fuel_price_per_litre
    income=no_of_passengers*ticket_price
    if income>expenditure:
        return income-expenditure
    else:
        return -1
        
#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=1
print(calculate(distance,no_of_passengers))
