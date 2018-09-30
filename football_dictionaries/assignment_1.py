import csv
from csv_example import read_squad_file
from pprint import pprint
# Data

squad = read_squad_file(file_name='squads.csv')


def players_as_dictionaries(squad):
    sq_list = []
    
    for player in squad:
        player_dict = {
            'caps': player[-5],
            'club': player[-4],
            'club_country' : player[-2],
            'country' : player[-3],
            'date_of_birth' : player[3],
            'name': player[2],
            'number' : player[0],
            'position' : player[1],
            'year' : player[-1],
        }
    
        sq_list.append(player_dict)
    
    return sq_list
