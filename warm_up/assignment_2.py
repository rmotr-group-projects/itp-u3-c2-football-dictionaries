# PASSED warm_up assignment_2

def transform_user_list_to_dict(a_user):
    users = {
        'name': a_user[0],
        'email': a_user[1],
        'age': int(a_user[2]),
    }
    
    return users
     
#transform_user_list_to_dict(['Don', 'don@don.com', 27])