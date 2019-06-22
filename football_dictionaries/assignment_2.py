from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    results = {}
    player_dict = players_as_dictionaries(squads_list)
    for player in player_dict:
        results.setdefault(player['position'], [])
        results[player['position']].append(player)
    return results
