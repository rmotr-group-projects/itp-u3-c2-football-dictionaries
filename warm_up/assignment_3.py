def transform_multiple_users_to_dicts(multiple_users):
    users_list = []
    for a_user in multiple_users:
        user = {
            'name': a_user[0],
            'email': a_user[1],
            'age': a_user[2],
        }

        users_list.append(user)
    return  users_list

