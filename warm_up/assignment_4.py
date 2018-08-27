from pprint import pprint

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
    },{
        'name': 'Jason',
        'email': 'jason@rmotr.com',
        'age': 61
    }]
    
    
def group_users_by_email_domain(users):
    result = {}
    emails = []
    #domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'rmotr.com']
    
    
    for item in users:
        email = item['email']
        emails.append(email)
        
        # need to make the if statements into one for loop for the domains
        # update at a later date

        # @gmail.com
        if 'gmail.com' in email:
            gmail = 'gmail.com'
            email = gmail
            
        # @yahoo
        if 'yahoo.com' in email:
            yahoo = 'yahoo.com'
            email = yahoo
            
        # @hotmail
        if 'hotmail.com' in email:
            hotmail = 'hotmail.com'
            email = hotmail
        
        # @rmotr.com
        if 'rmotr.com' in email:
            rmotr = 'rmotr.com'
            email = rmotr
     
        
        result.setdefault(email, [])
        result[email].append(item)
        
    return(result)