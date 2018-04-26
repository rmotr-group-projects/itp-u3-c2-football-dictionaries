from football_dictionaries.squads_data import SQUADS_DATA
import collections

def players_as_dictionaries(squads_list):
    '''Return a collection of football player information'''
    
    team_lineup = []
    team_info = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
   
    for data_set in squads_list:
        player_bio = collections.OrderedDict()
    
        for data_index, data in enumerate(data_set):
            player_bio[team_info[data_index]] = data
        
        team_lineup.append(player_bio)
    
    return team_lineup
    

print(players_as_dictionaries(SQUADS_DATA))
    


