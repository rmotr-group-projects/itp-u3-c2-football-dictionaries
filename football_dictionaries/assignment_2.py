from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.squads_data import SQUADS_DATA
import collections

def players_by_position(squads_list):
    ''' Return a dictionary where football players are organized by position'''
    
    # all players that play for the football club
    players = players_as_dictionaries(squads_list)
    
    player_lineup = collections.OrderedDict()
    
    # filter any duplicate player_position in squads_list
    field_positions = tuple(set([data_set[1] for data_set in squads_list]))
    
    for field_spot in field_positions:
        
        player_lineup.setdefault(field_spot, [])
        # organize the players by the position they play
        for player in players:
            if player.get('position') == field_spot:
                player_lineup.get(field_spot).append(player)
               
    return player_lineup
    
print(players_by_position(SQUADS_DATA))

