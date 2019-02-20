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

def players_as_dictionaries(players):
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

squad_data_test = players_as_dictionaries(squad)


def players_by_country_and_position(squad_data):
    posArr = {'GK':[], 'FW':[], 'DF':[], 'MF':[]}
    arr = {}
    for person in squad_data:
        if person['country'] not in arr:
            arr[person['country']]=posArr
        if person['position']=='GK':
            arr[person['country']]['GK'].append(person)
        elif person['position']=='FW':
            arr[person['country']]['FW'].append(person)
        elif person['position']=='DF':
            arr[person['country']]['DF'].append(person)
        elif person['position']=='MF':
            arr[person['country']]['MF'].append(person)    
    return arr

players_by_pos_and_country = players_by_country_and_position(squad_data_test)
print(players_by_pos_and_country)