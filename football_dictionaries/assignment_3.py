from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    player_country = {}
    
    for player in players_as_dictionaries(squads_list):
        if player["country"] not in player_country:
            player_country.update({player["country"]:{}})
            player_country[player["country"]].update({player['position']:[]})
            player_country[player["country"]][player['position']].append(player)
        elif player["position"] not in player_country[player["country"]]:
            player_country[player["country"]].update({player['position']:[]})
            player_country[player["country"]][player['position']].append(player)
        else:
            player_country[player["country"]][player['position']].append(player)

    return player_country