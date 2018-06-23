def players_as_dictionaries(squads_list):
    items = ['number','position','name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    # items[0], items[1], items[2], items[3]
    result = []

    for k in squads_list: # k is each list
        e_dict= {}
        count = 0
        for value in k: # value is each item in k
            # e_dict[key] = value ==> {'number': value}
            e_dict[items[count]] = value
            count += 1
        result.append(e_dict) 
 
    return result
    

