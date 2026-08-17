"""
IBM Data Analyst Professional Certificate
Course 04 - Python for Data Science, AI & Development

Module 03 - Python Programming Fundamentals
Lab 01 - Conditions and Branching

Author : Charly Varghese
"""

# Dataset

players = [
    {"name": "Serena Williams", "sport": "Tennis", "achievements": 23},
    {"name": "Lionel Messi", "sport": "Soccer", "achievements": 7},
    {"name": "Michael Phelps", "sport": "Swimming", "achievements": 23},
    {"name": "Usain Bolt", "sport": "Athletics", "achievements": 8},
    {"name": "Roger Federer", "sport": "Tennis", "achievements": 20},
    {"name": "Cristiano Ronaldo", "sport": "Soccer", "achievements": 5},
]
## print(type(players))
## print(len(players))

## for player in players:
 ##   print(player)

## for player in players:
 ##   print (player["name"])

## for player in players:
##   if player["name"] == "Lionel Messi":
 ##       print (player)

## for player in players:
##     if player["achievements"] > 10:
##        print(player)    

##for player in players:
##   if player["name"] == "Lionel Messi":
##       if player["achievements"] > 10:
##           print("Player Name :", player["name"])
 ##           print("Sport       :", player["sport"])
 ##           print("Achievements:", player["achievements"])
 ##       else:
 ##           print("Lionel Messi does not have more than 10 achievements.")    

#for player in players:
 #   if player["sport"] == "Tennis" or player["achievements"] == 20:
 #       print("Player Name :", player["name"])
 #       print("Sport       :", player["sport"])
 #       print("Achievements:", player["achievements"])
 #       print("-" * 40)

for player in players:
    if player["achievements"] < 10 and player["sport"] != "Soccer":
        print("Player Name :", player["name"])
        print("Sport       :", player["sport"])
        print("Achievements:", player["achievements"])
        print("-" * 40)