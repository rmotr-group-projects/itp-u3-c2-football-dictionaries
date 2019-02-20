import csv
import os

def read_squad_file(file_name='test_data.csv'):
    squad = []
    with open(file_name) as fp:
        reader = csv.reader(fp)
        for line in reader:
            squad.append(line)

    return squad

squad = read_squad_file(file_name='test_data.csv')

def players_as_dictionaries(squad):
    retArr=[]
    for player in players:
            retArr.append({
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
            })
    return retArr
