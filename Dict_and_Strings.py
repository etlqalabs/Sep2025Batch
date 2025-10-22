'''
emp_set  = {1,2,3}
print(type(emp_set))
print(emp_set)

emp_dict = {3:"Ankita",1:"Arjun",2:"Aneela"}
print(type(emp_dict))
#print(emp_dict)

# get the employee's name of emo = 2
print(emp_dict[2])
print(emp_dict.get(2))

# add one more employee in to dict
emp_dict[4]="Malthi"
emp_dict[5]="Malthi"
print(emp_dict)

# update name of empid=1 with Akash
emp_dict[1]="Akash"
print(emp_dict)

# delete empid = 2
del emp_dict[2]
print(emp_dict)

emp_dict.pop(3)
print(emp_dict)

emp_dict.popitem()
print(emp_dict)



emp_dict = {3:"Ankita",1:"Arjun",2:"Aneela"}

# Get me all empno
all_keys = emp_dict.keys()
print("Data type of keys is ", type(all_keys), " and keys are ",all_keys)

# Get me all the names of emp
all_values = emp_dict.values()
print("Data type of keys is ", type(all_values), " and keys are ",all_values)

# Get me all the items
all_items = emp_dict.items()
print("Data type of item is ", type(all_items), " and items are ",all_items)

# print all the eno with emp name

for key,value in emp_dict.items():
    print(key, "=>>>",value)


employees = {1:"Alex",2:"Bob",3:"Charlie"}

for empno,ename in employees.items():
    print(empno,"=>>",ename)

# empty the dictionary
print(emp_dict)
emp_dict.clear()
emp_dict[1] = "Rakesh"
print(emp_dict)


# Strings

print(ord('A')) # 65+25=90
print(ord('Z')) # 65+25=90
print(ord('a')) # 97
print(ord('z')) # 97+25 = 122

print(chr(90))



# Way 1 : print me all the characters in this string
for ele in name:
    print(ele)


# way 2 : print me all the characters in this string
name = "ETL QA Labs"
l = len(name)
print("size of string is :",l)
for idx in range(0,l,1):
    print(name[idx])



# Print in the reverse order
name = "ETL QA Labs"
l = len(name)

start_idx = l-1
end_idx = 0

while start_idx >= end_idx :
    print(name[start_idx])
    start_idx=start_idx -1



student = {"Aman":"IT","Rakesh":"Mech","Aman":"CS"}
student["Pankaj"] = "Finance"
print(student)
'''


# write a program to determine whether the string contains any lowercase

name = "ETLQA"
for ele in name:
    num = ord(ele)
    if (num>97 and num<=122):
        print("There is lower case and that is ",chr(num))
        break

