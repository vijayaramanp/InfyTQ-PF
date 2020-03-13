
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

def place_order(*item_tuple):
    for i in range(0,len(item_tuple),2):
        item_name=item_tuple[i]
        if item_name in menu:
            if check_quantity_available(menu.index(item_name),item_tuple[i+1])==True:
                print(item_name,"is available")
            else:
                print(item_name,"stock is over")
                break
        else:
            print(item_name," is not available")
        
def check_quantity_available(index,quantity_requested):
    if quantity_requested<=quantity_available[index]:
        quantity_available[index]-=quantity_requested
        return True
    else:
        return False
#Provide different values for items ordered and test your program
place_order("Fried Rice",2,"Soup",2)
#place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)
