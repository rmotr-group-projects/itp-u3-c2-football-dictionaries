def group_users_by_email_domain(users):
    
    by_email = {} # defining the output dictionary which groups users by email domain
    
    
    # function to extract email domain from the user email
    def get_user_domain(email):
        email_domain = email[(email.index('@'))+1:] # + 1 because we don't want '@' in the key.
        return email_domain
        
    # this for loop is just populating by_email dictionary with all possible domains as keys from the users list
    
    for user in users: #This will give me a user dictionary from users list
        
        email_domain = get_user_domain(user['email'])
        
        """Checks to see if email domain exists or not in the by_email dictionary.
        If it doesn't exist, a key is created and user is added to that key. If it
        exists user is appended to the list in that key
        """
        
        if email_domain not in by_email.keys():
            
            by_email[email_domain] = [user]
            
        else:
            by_email[email_domain].append(user)
    
    return by_email
    

users = [{
        'name': 'John',
        'email': 'john@gmail.com',     # gmail
        'age': 31
    }, {
        'name': 'Mary',
        'email': 'mary@hotmail.com',   # hotmail
        'age': 28
    }, {
        'name': 'Rose',
        'email': 'rose@yahoo.com',     # yahoo
        'age': 30
    }, {
        'name': 'Jane',
        'email': 'jane@gmail.com',     # gmail
        'age': 25
    }, {
        'name': 'Dustin',
        'email': 'dustin@hotmail.com',  # hotmail
        'age': 35
    }]
    
print(group_users_by_email_domain(users))
     

        


