
from DJANGO__.blog.models import users,posts

#  authenticate
#  authenticate(username,email):


def authenticate(**kwargs): #kwargs={"username":"django","email":"django@gmail.com"}
    username=kwargs.get("username")
    email=kwargs.get("email")     # use "get function always"
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data

session={}

def login_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper
@login_required
def loged_user():
    username=session.get("user")
    user_id=[user["id"] for user in users if user["username"]==username[0]]
    return user_id

class SignInView:

    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("success")
            session["user"]=username
        else:
            print("invalid credentials")

@login_required
def logout(*args,**kwargs):
         session.pop("user")
         print("user logged out")

class PostListView:
    @login_required
    def get(self,*args,**kwargs):
        return posts

class MypostsView:
    @login_required
    def get(self,*args,**kwargs):
        username=session.get("user")
        userId=[user["id"] for user in users if user["username"]==username[0]]
        qs=[post for post in posts if post["userId"]==userId]
        return qs

user=SignInView()
user.post(username="django",email="django@gmail.com")

po=MypostsView()
print(po.get())

class postcreateview():
    @login_required
    def post(self,*args,**kwargs):
        userId=loged_user
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userId,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")

class postdetailsview():
    def get(self,*args,**kwargs):
        postId=kwargs.get("postId")
        qs=[ p for p in posts if p.get("id")==postId]
        return qs
    def put(self,id=None,*args,**kwargs):

        post=[p for p in posts if p.get("id")==id[0]]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)


usr=SignInView()
usr.post(username="django",email="django@gmail.com")
pst=postcreateview()
pst.post(title="mypost",body="this is my new post")

mp=MypostsView()
print(mp.get())  #(refer cls 23/06/2022)

detail=postdetailsview()
print(detail.get(postId=10))

detail.put(id=10,title="my new post",body="this is my post")


#sign=SignInView()
#sign.post(username="django",email="django@gmail.com")
#print(session)

pl=PostListView()
try:
    all_posts=pl.get()
except Exception as e:
    print(e)
logout()


#print(dir(dict))  to find all the methods in dictionary OR   dir(list) or dir(xx)  etc.
#OR print("pop" dir(dict))  ref cls 22/06/2022
#    if user_data:
#        return user_data
 #   else:
  #      return None

#print(authenticate("django","django@gmail.com"))