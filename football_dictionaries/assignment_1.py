
def players_as_dictionaries(squads_list):
    s_list = []
    
    for new_list in squads_list:
        squad = {
            'number': new_list[0],
            'position': new_list[1],
            'name': new_list[2],
            'date_of_birth': new_list[3],
            'caps': new_list[4],
            'club': new_list[5],
            'country': new_list[6],
            'club_country': new_list[7],
            'year': new_list[8]
        }
        s_list.append(squad)
    return s_list
        
        
'''
{
        'caps': '',
        'club': 'Quilmes',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
        'name': 'Juan Botasso',
        'number': '1',
        'position': 'GK',
        'year': '1930'
    }
'''        

