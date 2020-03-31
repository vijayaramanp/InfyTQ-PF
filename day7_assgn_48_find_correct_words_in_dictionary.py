#PF-Assgn-48

def find_correct(word_dict):
    correct_list=[0]*3
    for key,value in word_dict.items():
        if len(key) == len(value):
            difference=0
            for i in range(len(key)):
                if key[i]==value[i]:
                    continue
                else:
                    difference+=1
            if difference == 0:
                correct_list[0]+=1
            elif difference < 3:
                correct_list[1]+=1 
            else:
                correct_list[2]+=1
        else:
           correct_list[2]+=1 
    return correct_list

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
