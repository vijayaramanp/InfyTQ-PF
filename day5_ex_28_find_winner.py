#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    team1_won_count=match_tuple.count("Team1")
    team2_won_count=match_tuple.count("Team2")
    if team1_won_count>team2_won_count:
        return "Team1"
    elif team1_won_count==team2_won_count:
        return "Tie"
    else:
        return "Team2"

#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
#print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
