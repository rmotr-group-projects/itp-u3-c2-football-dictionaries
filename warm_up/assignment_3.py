user1 = ['john','jj@jj.com', 21]
user2 = ['pat', 'aw@jdj.com', 22]
user3 = ['jill', 'jd@jj.com', 32]

all_users = [user1, user2, user3]


def transform_multiple_users_to_dicts(multiple_users):
    
    # empty string to append to at end
    result = []
    
    
    for item in multiple_users:
        # empy dict to hold all parsed info
        users = {}
        # define variables
        name = item[0]
        email = item[1]
        age = item[2]
        
        # assign variables to dict
        users['name'] = name
        users['email'] = email
        users['age'] = age
        
        # update to empyt dict users and append that info to result
        #users.update(users)
        result.append(users)
    
    return result