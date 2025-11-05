class Student:

    def __init__(self,roll_no,student_name):
        self.roll_no = roll_no
        self.student_name = student_name

    school_name = "DPS"
    def attendClass(self):
        print(f"{self.student_name} attends class")

    @staticmethod
    def appear_for_exam():
        print("Studnet appears for exam")
'''
s1 =  Student(1,"Chandra")
print(s1.roll_no)
print(s1.student_name)

s1.attendClass()
s1.appear_for_exam()
'''

Student.appear_for_exam()