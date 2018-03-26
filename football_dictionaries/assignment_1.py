from squads_data import SQUADS_DATA as squads_list

new_squads_list = squads_list[:]

def players_as_dictionaries(squads_list):
    player_dict_format = []
    for player in new_squads_list:
        player_bio = {
            'number': None,
            'position': None,
            'name': None,
            'date_of_birth': None,
            'caps': None,
            'club': None,
            'country': None,
            'club_country': None,
            'year': None
        }
        for bio_info in player:
            player_bio[key] = bio_info
        player_dict_format.append(player_bio)
    return player_dict_format
    
players_as_dictionaries(squads_list)
    
