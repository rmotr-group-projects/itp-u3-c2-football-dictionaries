from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    players = players_as_dictionaries(squads_list)
    finaldict={}
    for item in range(len(players)):
        position = players[item]['position']
        finaldict.setdefault(position,[])
        finaldict[position].append(players[item])
    return finaldict
