from football_dictionaries.assignment_2 import players_by_position


def players_by_country_and_position(squads_list):
    answer = {
        'Argentina': {
                "GK": [],
                "FW": []
        },
        'Belgium': {
                "GK": [],
                "MF": [],
                "FW": []
        },
        'Brazil': {
                "MF": []
        },
        'South Korea': {
                "GK": [],
                "MF": [],
                "FW": []
        }
    }
    all_positions = players_by_position(squads_list)

    for position, player_list in all_positions.items():  # gives 3 keys
        for player in player_list:  # for each player in the position list
            # find the country they're in
            # find the position they have
            # put them in the proper country/position
            # if (player['country'] == 'Argentina') and (player['position'] == position) and (player not in answer['Argentina'][position]):
            #     answer['Argentina'][position].append(player)
            if (player['country'] == 'Argentina') and (player['position'] == position):
                answer['Argentina'][position].append(player)
            elif (player['country'] == 'Belgium') and (player['position'] == position):
                answer['Belgium'][position].append(player)
            elif (player['country'] == 'Brazil') and (player['position'] == position):
                answer['Brazil'][position].append(player)
            elif (player['country'] == 'South Korea') and (player['position'] == position):
                answer['South Korea'][position].append(player)
    
    # 2 argentina, 6 brazil
    return answer
