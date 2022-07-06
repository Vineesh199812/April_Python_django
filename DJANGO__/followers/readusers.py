from json import *

with open("users.json") as f:
    data=load(f)
print(len(data))

#followers of id 2

followers_user=[len(user["followers"]) for user in data if user["id"]==2]
print(followers_user)

#user with most followers

print(max(data,key=lambda user:len(user["followers"])))

#user with less following

print(min(data,key=lambda user:len(user["following"])))

#suggestions to follow  (cls 06/07/2022)

all_users=[user["id"]for user in data ]
my_followings=[user ["following"] for user in data if user["id"]==1]
my_following=my_followings.pop()

to_follow=[user for user in all_users if user not in my_following]

print(all_users)
print(my_following)
print(to_follow)
#OR
better_to_follow=set(all_users) - set(my_following)
print(better_to_follow)
