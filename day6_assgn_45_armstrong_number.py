#PF-Tryout
def find_armstrong(number):
    temp = 0
    num = number
    while(number!=0):
        remainder=number%10
        number=number//10
        temp+=(remainder*remainder*remainder)
    if(num==temp):
        return True
    return False

number=371
if(find_armstrong(number)):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")
