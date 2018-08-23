def transform_multiple_users_to_dicts(multiple_users):
    new_list=[]
    for i in multiple_users:
        new_dict={
        'name':i[0],
        'email':i[1],
        'age':i[2]
    }
        new_list.append(new_dict)
    return new_list
