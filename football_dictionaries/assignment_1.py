from .squads_data import SQUADS_DATA

def players_as_dictionaries(data):
    result = []
    if len(data) <=0 or data is None:
        return bad_data()
    keys = ['number', 'position', 'name', 'date_of_birth','caps', 'club', 'country',  'club_country', 'year'  ]
    #keys = ['position', 'name', 'country', 'club_country']
    for item in data:
        if item is None or len(item) <= 0 or len(item) > len(keys):
            return bad_data()
        player ={}
        for index, key in enumerate(keys):
            player[key] = item[index]
        result.append(player)
    return result

def bad_data():
    return 'Bad data'
