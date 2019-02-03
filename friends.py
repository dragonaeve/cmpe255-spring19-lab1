users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    # TODO
    if next((item for item in users if item["name"] == user), False):
        entry = next(item for item in users if item["name"] == user)
        num=0
        idnum = entry['id']
        for item in friendship:
            if idnum in item:
                num+=1
        return num
    else:
        print("User not found.")
        return -1
    pass

from operator import itemgetter

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    # TODO
    friendcount = [num_friends(user["name"]) for user in users]
    result = [dict(item, **{'friends': num_friends(item["name"])}) for item in users]
    print(sorted(result,key=itemgetter('friends','name'),reverse=True))
    pass