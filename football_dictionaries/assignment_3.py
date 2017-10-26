from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    whole_team = players_as_dictionaries(squads_list)
    result_country = {}
    for footballers in whole_team:
        country = footballers['country']
        position = footballers['position']
        result_country.setdefault(country, {})
        result_country[country].setdefault(position, [])
        result_country[country][position].append(footballers)
    return result_country