def transform_multiple_users_to_dicts(multiple_users):
    result=[]
    for user in multiple_users:
        result.append({
            'name':user[0],
            'email':user[1],
            'age':user[2]
        })
    return result