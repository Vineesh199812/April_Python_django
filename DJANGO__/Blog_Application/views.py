from DJANGO__.Blog_Application.models import users, posts


# authenticate
# username
# password

# username="anu"
# password="Password@123"
# user= {"id": 1, "username": "akhil", "email": "akhil@gmail.com", "password": "passwors@123"}

# user=[user for user in users if user["username"]==username and user["password"]==password]
#    print(user)  (REFER CLASS 28/06/2022)

def signin_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("u must login")
    return wrapper

session = {}

def authenticate(**kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user


#print(authenticate(username="anu", password="Password@123"))


class Signinview:
    username: str
    password: str  # (jst convey)

    def post(self, *args, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)
        if user:
            session["user"] = user[0]
            print("success")

        else:
            print("invalid")


class Postsview():
    @signin_required
    def get(self, *args, **kwargs):
        return posts

    @signin_required
    def post(self, *args, **kwargs):
        print(kwargs)
        userId = session["user"]["id"]
        kwargs["userId"] = userId
        posts.append(kwargs)
        print(posts)


class Mypostlistview():
    @signin_required
    def get(self, *args, **kwargs):
        print(session)
        userId = session["user"]["id"]
        print(userId)
        my_posts = [post for post in posts if post["userId"] == userId]
        return my_posts


class Postdetails():
    def get_object(self, post_id):
        post = [post for post in posts if post["postId"] == post_id]
        return post

    @signin_required
    def get(self, *args, **kwargs):
        post_id = kwargs.get("post_id")
        post = self.get_object(post_id)
        return post

    @signin_required
    def delete(self, *args, **kwargs):
        post_id = kwargs.get("post_id")
       # data=[post for post in posts if post["postId"]==post_id]
        data = self.get_object(post_id)
        if data:
            post = data[0]
            posts.remove(post)
            print("post removed")
            print(len(posts))  # to know howmany posts are available after deleting
            for p in posts:  # to know and print the remaining posts
                print(p)

    @signin_required
    def put(self, *args, **kwargs):
        post_id = kwargs.get("post_id")
        data = kwargs.get("data")
        instance = self.get_object(post_id)
        if instance:
            post_obj = instance[0]
            post_obj.update(data)
            return post_obj


class Likeview:
    @signin_required
    def get(self,*args,**kwargs):
        postid = kwargs.get("postid")
        post = (post for post in posts if post("postId") == postid)
        if post:
            post=posts[0]
            userId=session["user"]["id"]
            post["liked_by"].append(userId)
            print(post)


log = Signinview()
log.post(username="richard", password="Password@123")
print(session)
data=Postsview()
print(data.get())
data.post(postId=9,
         title="hello there",
         content="abcd@123",
         liked_by=[])
myposts = Mypostlistview()
print(myposts.get())

post_detail = Postdetails()
# post_detail.delete(post_id=6)
print(post_detail.get(popst_id=6))
post_detail.delete(post_id=6)
data = {
    "title":"newtitle"
}
postdetails = Postdetails()
print(postdetails.put(post_id=4, data=data))

like = Likeview()
like.get(post_id=6)
#print(like.get())

# GET =>retrive
# POST =>create
# PUT/PATCH =>edit
# DELETE =>delete
