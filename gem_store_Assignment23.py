#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for i in range(0,len(reqd_gems)):
        if reqd_gems[i] in gems_list:
            if reqd_quantity[i]>0:
                indx=gems_list.index(reqd_gems[i])
                bill_amount=bill_amount+(price_list[indx]*reqd_quantity[i])
        else:
            bill_amount=-1
            break
    if bill_amount>30000:
        bill_amount=bill_amount-(bill_amount*0.05)
            
                
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[100,200,300,400,500]

#List of gems required by the customer
reqd_gems=["Abc","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,1,1]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
