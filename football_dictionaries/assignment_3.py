    from football_dictionaries.assignment_3 import players_by_country_and_position
    def players_as_dictionaries(squads_list):
    users = []
    for user in squads_list:
        user_dict = {
            'number': user[0],
            'position': user[1],
            'name': user[2],
            'date_of_birth': user[3],
            'caps': user[4],
            'club': user[5],
            'country': user[6],
            'club_country': user[7],
            'year': user[8],
        }
        users.append(user_dict)
    return users

def players_by_country_and_position(squads_list):
    country_position_dict = {}
    players = players_as_dictionaries(squads_list)
    
    for player in players:
        country = player['country']
        position = player['position']
        country_position_dict.setdefault(country, {})
        country_position_dict[country].setdefault(position, [])
        
        country_position_dict[country][position].append(player)

    
    return country_position_dict




