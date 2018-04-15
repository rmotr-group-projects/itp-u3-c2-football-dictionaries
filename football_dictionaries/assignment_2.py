from football_dictionaries.assignment_1 import players_by_dictionaries

def players_by_position(squads_list):
    
    position_list = set()

    for players in squads_list:
    	position_list.add(players[1])

    position_dict = {}

    for position in position_list:

    	positions = []

    	for players in squads_list:
    		if position in players:
    			positions.append(players)

    	position_dict[position] = players_by_dictionaries(positions)

    return position_dict

