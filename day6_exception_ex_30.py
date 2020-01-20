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
