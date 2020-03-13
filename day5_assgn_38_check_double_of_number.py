#PF-Assgn-38
def check_double(number):
    double_of_number=2*number
    str_num=str(number)
    str_dbl_num=str(double_of_number)
    if len(str_num)==len(str_dbl_num):
        for i in range(0,len(str_num)):
            if str_num[i] in str_dbl_num:
                continue
            else:
                return False 
    else:
        return False
        
    return True
#Provide different values for number and test your program
print(check_double(9))
