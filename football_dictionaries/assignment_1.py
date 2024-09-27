def players_as_dictionaries(squad):
    result = []
    for entry in squad:
        player = {
            'caps': entry[4],
            'club': entry[5],
            'club_country': entry[7],
            'country': entry[6],
            'date_of_birth': entry[3],
            'name': entry[2],
            'number': entry[0],
            'position': entry[1],
            'year': entry[8],
        }
        result.append(player)
    return result
    