class course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
    @property #(ref cls 27/06/2022)
    def get_name(self):
        return self.course_name

    def __str__(self):
        return self.course_name

class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.student_name

django=course()
django.add_course(course_name="django",status=True)
bd=course()
bd.add_course(course_name="bigdata",status=True)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2k22b1",start_date="12-06-2022")

vishnu=Student()
vishnu.add_student(student_name="vishnu",email="vishnu1998@gmail.com",batch=djb1)

rahul=Student()
rahul.add_student(student_name="rahul",email="rahul1998@gmail.com",batch=djb1)

akhil=Student()
akhil.add_student(student_name="akhil",email="akhil1998@gmail.com",batch=djb1)

mearnstack=course()
mearnstack.add_course(course_name="mearnstack",status=True)
msb1=Batch()
msb1.add_batch(course=mearnstack,batch_code="msmay2k22b1",start_date="12-06-2022")


ravi=Student()
ravi.add_student(student_name="ravi",email="ravi1998@gmail.com",batch=msb1)

vinay=Student()
vinay.add_student(student_name="vinay",email="vinay1998@gmail.com",batch=msb1)

students=[]
students.append(ravi)
students.append(rahul)
students.append(vinay)
students.append(vishnu)


#print students in mearnstack

for stud in students:
    if stud.batch.course.course_name=="mearnstack":
        print(stud)

        #OR

ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="mearnstack"]
print(ms_stud)