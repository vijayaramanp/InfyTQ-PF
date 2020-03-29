#PF-Tryout
#Start writing your code here
import random
probability=0.7
for i in range(1,7):
    if random.random()<=probability:
        print("Head")
    else:
        print("Tail")
    
