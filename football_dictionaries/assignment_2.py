# from assignment_1 import players_as_dictionaries

""" Note: For some reason, tests.py didn't like me importing the function 
    from assignment_1, so the first function is an iteration of the one found in
    that assignment."""
    
    
def players_as_dictionaries(squads_list):
    # Returns info of players of a squad into a dictionary
    overall_squad_bio = []
    player_bio_info = [
        'number',
        'position',
        'name',
        'date_of_birth',
        'caps',
        'club',
        'country',
        'club_country',
        'year'
    ]
    for player in squads_list:
        """Uses the zip function to combine player_bio_info with player info lists 
           and then turns it into a dictionary"""
        combined_lists_dict = dict(zip(player_bio_info, player))
        overall_squad_bio.append(combined_lists_dict)    
    return overall_squad_bio

def players_by_position(squads_list):
    #Uses previous assignment function for base
    new_squads_list = players_as_dictionaries(squads_list)
    player_position_dict = {
        'GK': [],
        'MF':[],
        'FW': []   
    }
    for player in new_squads_list:
        # Appends player dictionary to a new position dictionary
        if player['position'] not in player_position_dict:
            continue
        else:
            player_position_dict[player['position']].append(player)
    return player_position_dict




    
    
    
