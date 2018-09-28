from .assignment_2 import transform_user_list_to_dict

def transform_multiple_users_to_dicts(multiple_users):
    all_users = []
    for user in multiple_users:
        all_users.append(transform_user_list_to_dict(user))
    return all_users
        
