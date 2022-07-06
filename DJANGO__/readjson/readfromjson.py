
# import from json
# json.load()

from json import*

with open ("blog.json","r",encoding='utf-8') as f:
    data=load(f)
print(data)

user_posts=[post for post in data if post["userId"]==1]
print(len(user_posts))

#no. of likes for postId=3

user_likes=[len(post["liked_by"]) for post in data if post["postId"]==3]
print(user_likes)

#no.of posts liked by userId=2

like_count_user=len([post for post in data if 2 in post["liked_by"]])
print(like_count_user)

#posts which have most likes

print(max(data,key=lambda post:len(post["liked_by"])))