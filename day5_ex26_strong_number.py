#PF-Exer-26

def factorial(number):
    fact=1
    if number==0 or number==1:
        return 1
    else:
        while number>0:
            fact=fact*number
            number=number-1
        return fact
    

def find_strong_numbers(num_list):
    strong_list=[]
    
    for i in num_list:
        if i!=0:
            
            num=i
            str_num=0
            while num!=0:
                fact=num%10
                str_num=str_num+factorial(fact)
                num=num//10
            if i==str_num:
                strong_list.append(i)
    return strong_list


num_list=[145,2,0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
