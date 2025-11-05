class Student:
    def __init__(self):
        print("I am default constrcutor..")

    def __init__(self,roll_no,student_name):
        self.roll_no = roll_no
        self.student_name = student_name

    school_name = "DPS"
    def attendClass(self):
        print(f"{self.student_name} attends class")


#s1 = Student()
#print("School name :" ,s1.school_name)
#s1.attendClass()

s2 = Student(1,"Chandra")
print(s2.roll_no)
print(s2.student_name)
print(s2.school_name)
s2.attendClass()

s3 = Student(2,"Alex")
print(s3.roll_no)
print(s3.student_name)
print(s2.school_name)
s3.attendClass()

s2.roll_no = 10

print(s2.roll_no)
print(s2.student_name)

print(s3.roll_no)
print(s3.student_name)

