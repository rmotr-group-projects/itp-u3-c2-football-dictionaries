from squads_data import SQUADS_DATA
from .assignment_2 import players_by_position



def players_by_country_and_position(squads_list):
    positions = []
    countries = []
    result = {
     'Belgium': {},
     'Brazil': {},
     'Argentina': {},
     'South Korea': {},   
      }
    #create list(countries) with possible countries
    for player in squads_list:
        country = player[-3]
        if country not in countries:
            countries.append(country)
    #create list(positions) with possible positions
    for player in squads_list:
        position = player[1]
        if position not in positions:
            positions.append(position)


    argentina = []
    belgium = []
    brazil = []
    skorea = []
    #separate players by country with player[-3] from input
    for player in squads_list:
        if player[-3] == 'Argentina':
            argentina.append(player)
        elif player[-3] == 'Belgium':
            belgium.append(player)
        elif player[-3] == 'Brazil':
            brazil.append(player)
        else:
            skorea.append(player)

    #use players_by_position to separate each countries' players by position
    sun_of_may = players_by_position(argentina)
    black_lion = players_by_position(belgium)
    ordem_e_progresso = players_by_position(brazil)
    taegukgi = players_by_position(skorea)


    #update the first half with the second
    result['Argentina'].update(sun_of_may)
    result['Belgium'].update(black_lion)
    result['Brazil'].update(ordem_e_progresso)
    result['South Korea'].update(taegukgi)

    #iterate through countries and positions to find and del any result[country][position] == []
    for country in countries:
        #print(country)
        for position in positions:
            #print(position)
            if result[country][position] == []:
                del result[country][position]
                
    #Miller time
    return result