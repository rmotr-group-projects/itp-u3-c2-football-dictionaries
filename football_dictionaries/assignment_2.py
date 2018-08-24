def players_by_position(squads_list):
    grouped_dict = {}

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
        grouped_dict.setdefault(play_dict['position'], [])
        grouped_dict[play_dict['position']].append(play_dict)
    
    return grouped_dict

