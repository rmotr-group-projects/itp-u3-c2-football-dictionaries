def group_users_by_email_domain(users):
    grouped_users = {}

    for user in users:
        email_full = user['email']
        email_full_split = email_full.split('@')
        email_domain = email_full_split[1]

        grouped_users.setdefault(email_domain, [])
        grouped_users[email_domain].append(user)

    return grouped_users