from warm_up.assignment_2 import transform_user_list_to_dict

def transform_multiple_users_to_dicts(multiple_users):
    
    user_list = []
    
    for user in multiple_users:
        
        user_list.append(transform_user_list_to_dict(user))
        
    return user_list
        
        
        
        
