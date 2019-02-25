from football_dictionaries.squads_data import SQUADS_DATA
def players_as_dictionaries(squads_list):
    players_list = []
    for player in squads_list:    
        players_dictionaries = {
            'caps': player[4],
            'club': player[-4],
            'club_country': player[-2],
            'country': player[-3],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[-1],
            }
        players_list.append(players_dictionaries)
        
    return players_list
