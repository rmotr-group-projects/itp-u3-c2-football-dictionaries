# from football_dictionaries.squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    result = []
    for player in squads_list:
        players_as_dict = {
                'number': player[0],
                'position': player[1],
                'name': player[2],
                'date_of_birth': player[3],
                'caps': player[4],
                'club': player[5],
                'country': player[6],
                'club_country': player[7],
                'year': player[8]
            }
        result.append(players_as_dict)
        
    return result
# print(players_as_dictionaries(squads_list))