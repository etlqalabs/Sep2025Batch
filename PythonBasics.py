#Variable used to store values ( data elements )
'''
nameofstudent = "Abhinav"
ageOfStudent = 25
elligible_for_vote = True
'''
# Naming conventions
# 1) Camel Case : each word starts with upper case except first word
# e.g. nameOfStudent = "Abhinav"

# 2) Pascal Case : each word starts with upper case
# e.g. NameOfStudent = "Abhinav"

# 3) Snake Case : each word will be seperated by _
# e.g. name_of_student = "Abhinav"
'''

nameOfStudent = "Abhinav"
ageOfStudent = 25
elligibleForVote = True

print("Studnet name is :",nameOfStudent," and Age of the Student is :",ageOfStudent,
      " and student is ellibigle for voting : ",elligibleForVote)


# Type Casting ( converting data from one to another type ) e.g. string value to int

age = "25"
age_of_student = 25
print("Age is of type : ",type(age))
print("Age of Student is of type : ",type(age_of_student))

# convert the age from string type to integer
age_converted =  int(age)
print("converted Age is of type : ",type(age_converted))

marks1 = "50"
marks2 = "60"
total_marks = marks1 + marks2
print("Total marks : ",total_marks)

total_marks_conv = int(marks1) + int(marks2)
print("Total marks converetd  : ",total_marks_conv)

# upcasting ( converting lower data type to higher data type )
weight_of_person_int = 75
print("Weight is float ",float(weight_of_person_int))

# downcasting ( converting higher data type to lower data type )
weight_of_person_float = 75.8
print("Weight is int ",int(weight_of_person_float))


# Control Statements ( if..else..elif ( else if ) )
# if statement
age = 20

if age > 18:
    print("Person is eliigible for voting")
    

# if . else  statement
age = 18

if age >=18:
    print("Person is eliigible for voting")
else:
    print("Person is not eliigible for voting")



# if . elif statement
age = 110

if age < 18:
    print("Person is not elligible for voting")
elif age >=18 and age < 95:
    print("Person is eliigible for voting")
else:
    print("Person is super senior citizen..")


# Print ETL QA labs 10 times
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")
print("ETL QA Labs")

# Using FOR loop
# range(10) => strats from 0 and goes up to 10-1 (9) . 0 to 9 = 10 times
for val in range(1,10):
    print(val,": ETL QA Labs")



# while ( Execute until its true )
print("While loop demo :")
start = 1
end = 10
while ( start < end ):
    print(start, ": ETL QA Labs")
    start = start + 1
'''
