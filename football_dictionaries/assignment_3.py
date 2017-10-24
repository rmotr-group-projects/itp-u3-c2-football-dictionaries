from assignment_1 import players_as_dictionaries
from assignment_2 import players_by_position


def players_by_country_and_position(squads_list):
    countries = {}
    # get results from previous assignments
    formatted_list = players_as_dictionaries(squads_list)
    positions_list = players_by_position(squads_list)

    # iterate through the formatted list of players
    for player in formatted_list:
        # add countries to the collection
        countries.setdefault(player['country'], {})
        # iterate through each country and check it against
        # each country that the player is associated with
        # if there's a match add that players position to the
        # country, and passing an empty array as the default
        for country in countries:
            if (player['country'] == country):
                countries[country].setdefault(player['position'], [])
                countries[country][player['position']].append(player)

    return countries
