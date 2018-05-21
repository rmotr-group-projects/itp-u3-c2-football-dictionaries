def players_by_position(squads_list):
    result = {}

    for p in squads_list:
    	player = {
    		'number': p[0],
    		'position': p[1],
    		'name': p[2],
    		'date_of_birth': p[3],
    		'caps': p[4],
    		'club': p[5],
    		'country': p[6],
    		'club_country': p[7],
    		'year': p[8]
    	}

    	result.setdefault(player['position'], [])

    	result[player['position']].append(player)

    return result
