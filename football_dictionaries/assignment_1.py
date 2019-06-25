
def players_as_dictionaries(stuff):
    players_list = []
    number_of_players = len(stuff)
    for player in range(number_of_players):
        players_list.append({
            'number':stuff[player][0],
            'position':stuff[player][1],
            'name':stuff[player][2],
            'date_of_birth':stuff[player][3],
            'caps':stuff[player][4],
            'club':stuff[player][5],
            'country':stuff[player][6],
            'club_country': stuff[player][7],
            'year':stuff[player][8]                           
        })
    return players_list