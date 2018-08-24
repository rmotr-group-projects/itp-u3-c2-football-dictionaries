def players_as_dictionaries(squads_list):
    list_dicts = [] 

    for player in squads_list:
        number, position, name, date_of_birth, caps, club, country, club_country, year = player
        play_dict = {
            'number': number,
            'position': position,
            'name': name,
            'date_of_birth': date_of_birth,
            'caps': caps,
            'club': club,
            'country': country,
            'club_country': club_country,
            'year': year,
        }
        list_dicts.append(play_dict)
    
    return list_dicts


