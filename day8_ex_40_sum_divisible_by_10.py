#PF-Exer-40
#This verification is based on string match.

num1=20
num2=30

div = lambda x,y:x+y

if(div(num1,num2)%10)==0:
    print("Divisible by 10")
else:
    print("Not Divisible by 10")


def sum_all(function, data):
    result_sum=0;
    for w in data:
        if(function(w)):
            result_sum = result_sum+ w
    return result_sum

Q=[1,3,4,5,6,7,8,9,10,15,20]

p = lambda x:x

q = lambda x : x%2 == 0

r = lambda x : x%3 == 0

s = lambda x : x%5 == 0 


print(sum_all(p,Q))
print(sum_all(q,Q))
print(sum_all(r,Q))
print(sum_all(s,Q))
