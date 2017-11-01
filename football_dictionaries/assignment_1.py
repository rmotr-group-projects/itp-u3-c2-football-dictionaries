def players_as_dictionaries(squads_list):
    # labels
    labels = [
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
    # will contain formatted list of dictionaries
    formatted_list = []

    # returns a collection of dictionaries with labels as keys
    # and values set to None
    for player_info in squads_list:
        player = dict.fromkeys(labels)
        formatted_list.append(player)

    # iterate over the squads list array
    for index, player in enumerate(squads_list):
        # iterate through the players in squads_list, and labels
        # updates the formatted list with individual player info
        for info, label in zip(player, labels):
            formatted_list[index].update({label: info})

    return formatted_list
