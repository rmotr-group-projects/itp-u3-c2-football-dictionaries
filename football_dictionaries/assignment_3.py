#from football_dictionaries.assignment_1 import players_as_dictionaries

def players_as_dictionaries(squads_list):
    football_list=[]
    for player in squads_list:
        football_player={
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
        football_list.append(football_player)
    return football_list


def players_by_country_and_position(squads_list):
    result={}
    football_list=players_as_dictionaries(squads_list)
    
    for player in football_list:
        country=player['country']
        result.setdefault(country,{})
        position=player['position']
        result[country].setdefault(position,[])
        result[country][position].append(player)
        
    return result