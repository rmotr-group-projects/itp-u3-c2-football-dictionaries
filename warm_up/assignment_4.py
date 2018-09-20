def group_users_by_email_domain(users):
    emails = []
    holder = {}
    for user in users:
        domain = user['email'].split('@')[1].rstrip()
        if not domain in emails:
            holder[domain] = []
            emails.append(domain)
        holder[domain].append(user)
    return holder

