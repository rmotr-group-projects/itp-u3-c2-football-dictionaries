from squads_data import SQUADS_DATA
# from football_dictionaries.squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries
# from football_dictionaries.assignment_1 import players_as_dictionaries
from assignment_2 import players_by_position
# from football_dictionaries.assignment_2 import players_by_position
from pprint import pprint


def players_by_country_and_position(squads_list):
    players = players_as_dictionaries(squads_list)
    players_country_and_position = {}

    for player in players:
        # print(player)
        players_country_and_position.setdefault(player['country'], {})
        for country in players_country_and_position.keys():
            if country in player['country']:
                players_country_and_position[country][player['position']] = []
                players_country_and_position[country][player['position']].append(player)

    pprint(players_country_and_position)
players_by_country_and_position(SQUADS_DATA)
