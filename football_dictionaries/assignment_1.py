from football_dictionaries.squads_data import SQUADS_DATA
def players_as_dictionaries(squads_list):
    list_names = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    return [dict(zip(list_names, a_list)) for a_list in squads_list]
