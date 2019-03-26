from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    player_dict = players_as_dictionaries(squads_list)
    
    result={}
    
    for player in player_dict:
        country=player['country']
        position=player['position']
        result.setdefault(country, {})
        result[country].setdefault(position,[])
        result[country][position].append(player)
        
    return result

#     result={
#         'Argentina' : [],
#         'Belgium' : [],
#         'Brazil' : [],
#         'South Korea' : []
#     }

#     for position in pos_dic:
#         for i in range(len(position)):
#             if pos_dic[position][i]['country']=='Argentina':
#                 result['Argentina'].append({position: pos_dic[position]})
#             if pos_dic[position][i]['country']=='Belgium':
#                 result['Belgium'].append({position: pos_dic[position]})
#             if pos_dic[position][i]['country']=='Brazil':
#                 result['Brazil'].append({position: pos_dic[position]})
#             if pos_dic[position][i]['country']=='South Korea':
#                 result['South Korea'].append({position: pos_dic[position]})

    return result
        