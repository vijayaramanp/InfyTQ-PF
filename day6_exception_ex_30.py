# Below code passess all test cases

def find_average(mark_list):
	total=0
	try:
	    for i in range(0, len(mark_list)):
	        total+=mark_list[i]
	    marks_avg=total/len(mark_list)
	    return marks_avg
	except TypeError:
	    print("Wrong data type")
	except NameError:
	    print("Name Error")
	except ZeroDivisionError:
	    print("ZeroDivisionError")
	except IndexError:
	    print("index our of range")

try:
    m_list=[15,26,34,24]
    print("Average marks:", find_average(m_list))
except NameError:
    print("Name Error from main")
except TypeError:
    print("Type error from main")
except ValueError:
    print("value error from main")
'''

# statment 3 case 2
#PF-Exer-30

def find_average(mark_list):
	total=0
	try:
	    for i in range(0, len(mark_list)):
		    total+=mark_list[i]
	    marks_avg=total/len(mark_list)
	    return marks_avg
	except ZeroDivisionError:
	    print("Zero ZeroDivisionError")
	except TypeError:
	    print("Type Error")
	except IndexError:
	    print("Index Error")
try:
    m4="A"
    m4=int("A")
    m_list=[1,2,3,m4]
    print("Average marks:", find_average(m_list))
except:
    print("Some Error")

#Statement 3 case 3

#PF-Exer-30

def find_average(mark_list):
	total=0
	try:
	    for i in range(0, len(mark_list)):
	        total+=mark_list[i]
	    marks_avg=total/len(mark_list)
	    return marks_avg
	except TypeError:
	    print("Wrong data type")
	except NameError:
	    print("Name Error")

try:
    mark1="A"
    mark1=int("A")
    m_list=[mark1,2,3,4]
    print("Average marks:", find_average(m_list))
except NameError:
    print("Name Error from main")
except TypeError:
    print("Type error from main")
except ValueError:
    print("value error from main")

# statement 3 case 3
#PF-Exer-30

def find_average(mark_list):
	total=0
	try:
	    for i in range(0, len(mark_list)+1):
	        total+=mark_list[i]
	    marks_avg=total/len(mark_list)
	    return marks_avg
	except TypeError:
	    print("Wrong data type")
	except NameError:
	    print("Name Error")
	except ZeroDivisionError:
	    print("ZeroDivisionError")
	except IndexError:
	    print("index our of range")

try:
    m_list=[]
    print("Average marks:", find_average(m_list))
except NameError:
    print("Name Error from main")
except TypeError:
    print("Type error from main")
except ValueError:
    print("value error from main")
'''
