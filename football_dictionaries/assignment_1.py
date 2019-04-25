#from pprint import pprint

def players_as_dictionaries(squads_list):

    squads = []

    for squad in squads_list:
        caps= squad[4]
        club=  squad[5]
        club_country=  squad[-2]
        country= squad[-3]
        date_of_birth= squad[3]
        name= squad[2]
        number=squad[0]
        position= squad[1]
        year= squad[-1]
    
        squad={
            'caps': caps,
            'club': club,
            'club_country': club_country,
            'country': country,
            'date_of_birth': date_of_birth,
            'name': name,
            'number': number,
            'position': position,
            'year': year
            }
        squads.append(squad)
    return squads

#pprint (players_as_dictionaries(SQUADS_DATA))


"""
result = [
                {'caps':
                'club':
                ...
                },
                {},
                {}...
                
]
    
    
"""
    
