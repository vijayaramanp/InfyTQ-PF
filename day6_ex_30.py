

#problem 3.1

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
