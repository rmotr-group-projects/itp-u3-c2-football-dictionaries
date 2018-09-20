def transform_multiple_users_to_dicts(multiple_users):
    holder = []
    for user in multiple_users:
        holder.append({'name':user[0],'email':user[1],'age':user[2]})
    return holder

