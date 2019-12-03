#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    next_day=0 
    next_month=0 
    next_year=0
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
        if day>0 and day <31:
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1 
            next_month=month+1 
            next_year=year
    elif month==2:
        if day>0 and day <27:
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1 
            next_month=month+1 
            next_year=year
    elif month==4 or month==6 or month==9 or month==11:
        if day>0 and day <30:
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1 
            next_month=month+1 
            next_year=year
    else:
        if day>0 and day <31:
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1 
            next_month=1 
            next_year=year+1
        

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(30,12,2015)
