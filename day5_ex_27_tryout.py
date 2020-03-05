#PF-Tryout

def withdraw_transcation(amount,account_number,value):
    balance=balance_list[value]
    new_balance=balance-amount
    if(new_balance >= 500):
        balance_list[value]=new_balance
        print("Transaction completed successfully")
        print("Balance Amount :", new_balance)
    else:
        print("Insufficient Balance")
    

def deposit_transcation(amount,account_number,value):
        balance=balance_list[value]
        new_balance=balance+amount
        balance_list[value]=new_balance
        print("Transaction completed successfully")
        print("Balance Amount :", new_balance)
        
def balance_enquiry(account_number,value):
    balance=balance_list[value]
    print(balance)
    
def validate_account_number(account_number,amount):
    flag=None 
    value=0
    for index in range(0,len(account_list)):
        if(account_list[index]==account_number):
            flag=True
            value=index
            break
    if flag==True:
        if(transaction_type=="Withdraw"):
            withdraw_transcation(amount,account_number,value)
        elif(transaction_type=="Deposit"):
            deposit_transcation(amount,account_number,value)
        elif(transaction_type=="Balance Enquiry"):
            balance_enquiry(account_number,value)
        else:
            print("Invalid Transaction Type")
            
    
account_list=[1001,1002,1003,1004,1005]
balance_list=[2500,10000,7000,1500,500]
amount=1000
account_number=1003
transaction_type="Balance Enquiry"

validate_account_number(account_number,amount)
