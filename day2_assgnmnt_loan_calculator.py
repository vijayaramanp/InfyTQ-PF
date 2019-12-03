#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    flag=0
    #Start writing your code here
    if account_number>999 and account_number<2000:
        if account_balance>=99999:
            if loan_type=="Car" and salary>25000:
                if customer_emi_expected<=36 and loan_amount_expected<=500000:
                    eligible_loan_amount=500000
                    bank_emi_expected=36
                    flag=1
                else:
                    print("The customer is not eligible for the loan")
                    
            elif loan_type=="House" and salary>50000:
                if customer_emi_expected<=60 and loan_amount_expected<=6000000:
                    eligible_loan_amount=6000000
                    bank_emi_expected=60
                    flag=1
                else:
                    print("The customer is not eligible for the loan")
                    
            elif loan_type=="Business" and salary>75000:
                if customer_emi_expected<=84 and loan_amount_expected<=7500000:
                    eligible_loan_amount=7500000
                    bank_emi_expected=84
                    flag=1
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")

    #Use the below given print statements to display the output, in case of success
    if flag==1:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)

#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)
