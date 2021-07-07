from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(result):
    result_dict = players_as_dictionaries(result)
    final_answer = {}
    for item in result_dict:
        position_key = item.get('position')
        final_answer.setdefault(position_key, [])
        final_answer[position_key].append(item)
    return final_answer
