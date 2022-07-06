import random
#(refer cls 06/07/2022)

all_users=["a","b","c","d","e"]

def get_users():
    random.shuffle(all_users)
    return all_users[:3]
print(get_users())
