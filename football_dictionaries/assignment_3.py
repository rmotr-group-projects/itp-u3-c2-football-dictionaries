# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries
# Assignment 2
from football_dictionaries.assignment_2 import players_by_position


def players_by_country_and_position(squads_list):
            players = players_as_dictionaries(squads_list)
            result_dict = {}
            for player in players:
                country = player['country']
                position = player['position']
                result_dict.setdefault(country, {})
                result_dict[country].setdefault(position, [])
                result_dict[country][position].append(player)
            return result_dict


