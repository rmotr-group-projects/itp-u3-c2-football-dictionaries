def group_users_by_email_domain(multiple_users):
    users_dict = {}
    for user in multiple_users:
        domain = user['email'].split('@')[1]
        users_dict.setdefault(domain, [])
        users_dict[domain].append(user)
    return users_dict