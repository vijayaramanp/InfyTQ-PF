# PF-Assgn-56
# PF-Assgn-56
import re


def max_frequency_word_counter(data):
    data_dict = {}
    word = ""
    frequency = 0
    data = re.sub(r",", "", data).lower()
    while data:
        temp = data.split()
        for word in temp:
            count = temp.count(word)  # lis = re.findall(r"\b(?=\w)" + re.escape(word) + r"\b(?!\w)", data)
            if len(data_dict) == 0:
                data_dict.update({word: count})
                prev = word
            else:
                if count >= data_dict.get(prev):
                    data_dict.update({word: count})
                    prev = word
            temp1 = re.sub(r"\b(?=\w)" + re.escape(word) + r"\b(?!\w)", "", data)
            data = re.sub(r"  ", " ", temp1).strip()
            break

    print(data_dict)

    for key, value in data_dict.items():
        if value == frequency:
            if len(key) > len(word):
                word = key
                frequency = value

        elif value > frequency:
            word = key
            frequency = value
    print(word, frequency)


# Provide different values for data and test your program.
data = "Work like you do not need money, love like you have never you been hurt, and dance like no one is watching"
max_frequency_word_counter(data)


#<h3>Solution 2<h3>
# PF-Assgn-56
import re
def max_frequency_word_counter(data):
    data_dict = {}
    word = ""
    frequency = 0
    data = re.sub(r",", "", data).lower()
    while data:
        temp = data.split()
        for word in temp:
            lis = re.findall(r"\b(?=\w)" + re.escape(word) + r"\b(?!\w)", data)
            data_dict.update({word: len(lis)})
            temp1 = re.sub(r"\b(?=\w)" + re.escape(word) + r"\b(?!\w)", "", data)
            data = re.sub(r"  ", " ", temp1).strip()
            break
    maxx = 0
    prev = ''
    for key, value in data_dict.items():
        if value == maxx:
            if len(key) > len(prev):
                maxx = value
                word = key
                frequency = value
                prev = key
        elif value > maxx:
            maxx = value
            word = key
            frequency = value
            prev = key
    print(word, frequency)


# Provide different values for data and test your program.
data = "Work lik you do not need money, love lik your have never your been hurt, and dance like no one is watching"
max_frequency_word_counter(data)


#Solution 3
#PF-Assgn-56
#most frequent and lengthy word

def max_frequency_word_counter(data):
    word=""
    frequency=0
    data=data.lower()
    #data=data.replace(",","")
    lt=data.split()
    for e in lt:
        freq=lt.count(e)
        if freq > frequency :
            frequency=freq 
            word=e
        elif freq == frequency :
            if len(e) > len(word) :
                frequency=freq 
                word=e            
    print(word,frequency)
    
# Provide different values for data and test your program.
data = "Work lik you do not need money, love lik your have never your been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
