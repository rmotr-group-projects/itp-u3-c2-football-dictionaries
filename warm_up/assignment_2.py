from warm_up.assignment_1 import build_user_as_dict

def transform_user_list_to_dict(a_user):
    return {
        'name': a_user[0],
        'email': a_user[1],
        'age': a_user[2],
    }