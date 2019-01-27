from football_dictionaries.squads_data import SQUADS_DATA


def players_as_dictionaries(squads_list):
    result=[]
    list_names = [
        'number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    for a_list in squads_list:
        dictionary = dict(zip(list_names, a_list))
        result.append(dictionary)
    return result
# print(players_as_dictionaries(SQUADS_DATA))