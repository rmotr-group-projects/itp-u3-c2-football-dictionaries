"""
# code from
#https://stackoverflow.com/questions/31071888/python-group-list-items-in-a-dict

#Working / tested and passed.
"""


def players_by_position(squads_list):
    groupby_dict = {}
    new_squads_data = [
        {'number': x[0], 'position': x[1], 'name': x[2], 'date_of_birth': x[3], 'caps': x[4], 'club': x[5],
         'country': x[6], 'club_country': x[7], 'year': x[8], } for x in squads_list]
    print(new_squads_data)
    for e in new_squads_data:
        groupby_dict[e['position']] = groupby_dict.get(e['position'], [])
        groupby_dict[e['position']].append(e)
    return groupby_dict