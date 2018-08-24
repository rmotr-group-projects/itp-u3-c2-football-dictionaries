def players_by_country_and_position(squads_list):
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
        grouped_dict.setdefault(play_dict['country'], {})
        grouped_dict[play_dict['country']].setdefault(play_dict['position'], [])
        grouped_dict[play_dict['country']][play_dict['position']].append(play_dict)
    
    return grouped_dict
