#Caleb and Marcos

# we need to use the player_to_dict function from assignment_1.py so we import just it
from assignment_1 import player_to_dict
from squads_data import SQUADS_DATA as squad;

def players_by_position(squads_list):
    # create a dictionary which will house the different positions
    positions = dict()
    # loop over each player in squads_list, but just use the index
    for x in range(len(squads_list)):
        # for every possible position (squads_list[x][1]), create a new dictionary key if it does not already exist with the value of an empty list
        positions.setdefault(squads_list[x][1], [])
    # loop over each actual player (list) in squads_list
    for player_list in squads_list:
        # transform the player (list) to a player (dictionary)
        player_dict = player_to_dict(player_list)
        # if the player's position matches the position in the existing dictionary, append it to the list
        positions[player_dict['position']].append(player_dict)
    return positions
