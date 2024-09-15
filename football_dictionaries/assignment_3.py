from pprint import pprint

def players_by_country_and_position(squads_list):
    result = {}
    
    for player in squads_list:
        entry = {
            'caps': player[4],
            'club': player[5],
            'club_country': player[7],
            'country': player[6],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[8]
        }
        
        country = entry['country']
        position = entry['position']
        
        result.setdefault(entry['country'], {})
        result[country].setdefault(entry['position'], [])
        
        result[country][position].append(entry)
        
    
    # pprint(result)
    return result