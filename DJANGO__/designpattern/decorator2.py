def admin_permission_required(fn):

    def inner_fun(*args,**kwargs):
        user=kwargs.get("user")
        if user.role!="admin":
            raise Exception("permission denied")
        else:
            return fn(*args,**kwargs)

    return inner_fun

class User:

    def set_user(self,username,role):
        self.username=username
        self.role=role
    def print_details(self):
        print(self.username,self.role)

class AddCourse:

    @admin_permission_required
    def set_course(self,*ags,**kwargs):
        self.user=kwargs.get("user")
        self.course_name=kwargs.get("course_name")
    def print_details(self):
        print(self.course_name)

class AddBatch:
    @admin_permission_required
    def set_batch(self,*args,**kwargs):
        self.user=kwargs.get("user")
        self.batch_code=kwargs.get("b_code")
        self.course=kwargs.get("course")
    def print_details(self):
        print(self.batch_code)

user=User()
user.set_user("rahul","staff")

course=AddCourse()
course.set_course(user=user,coursename="django")

batch=AddBatch()
batch.set_batch(user=user,b_code="aprildjango2022",coure=course)

# Ctrl+Alt+L  to format documents properly.