#PF-Tryout
#Start writing your code here
import random
probability=0.7
for i in range(1,1001):
    if random.random()<=probability:
        print("Head")
    else:
        print("Tail")
    
    
'''Testing

#PF-Tryout
#Start writing your code here
import random
probability=0.7
lis=[0]*2
for i in range(1,1001):
    if random.random()<=probability:
        lis[0]+=1
    else:
        lis[1]+=1
print(lis)
'''
