from football_dictionaries.squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    players=[]
    for squad in squads_list:
        player_dict={
            'caps':squad[4],
            'club':squad[-4],
            'club_country':squad[-2],
            'country':squad[-3],
            'date_of_birth':squad[3],
            'name':squad[2],
            'number':squad[0],
            'position':squad[1],
            'year':squad[-1]
            
        }
        players.append(player_dict)
    return players