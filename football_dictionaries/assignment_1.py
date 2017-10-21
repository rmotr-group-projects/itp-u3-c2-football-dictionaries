def players_as_dictionaries(squads_list):
    new_squads_data = [{'number': x[0], 'position': x[1], 'name': x[2], 'date_of_birth': x[3], 'caps': x[4], 'club': x[5], 'country': x[6], 'club_country': x[7], 'year': x[8],} for x in squads_list]
    return new_squads_data


from football_dictionaries.squads_data import SQUADS_DATA
squads_list = SQUADS_DATA
testcode = players_as_dictionaries(squads_list)
print(testcode)
