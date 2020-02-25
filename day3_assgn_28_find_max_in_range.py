#PF-Assgn-28

def is_sum_multiple_of_three(num):
    summ=0 
    while num!=0:
        summ=summ+num%10 
        num=num//10
    if summ%3==0:
        return True
    else:
        return False

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    list1=[]
    if num1<num2:
        for num in range(num1,num2+1):
            if num%5==0 and num>9 and num<100 and is_sum_multiple_of_three(num)==True:
                list1.append(num)
              
        if len(list1)>0:
            max_num=max(list1)  
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(14,2)
print(max_num)
