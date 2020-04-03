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
