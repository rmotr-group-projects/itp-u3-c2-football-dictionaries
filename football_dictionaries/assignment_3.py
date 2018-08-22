def players_by_country_and_position(squads_list):
        country_and_position = {}
        for player in squads_list:
            player_dict = {
                'number': player[0],
                'position': player[1],
                'name': player[2],
                'date_of_birth': player[3],
                'caps': player[4],
                'club': player[5],
                'country': player[6],
                'club_country': player[7],
                'year': player[8],
            }
            country = player_dict['country']
            position = player_dict['position']

            country_and_position.setdefault(country, {})
            country_and_position[country].setdefault(position, [])
            country_and_position[country][position].append(player_dict)

        return country_and_position
