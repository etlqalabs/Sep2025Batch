# Collection/Sequence data types
'''
# List:
a) ordered collection of items ( the order in which data is stored)
b) Mutable ( which can be changed )
c) Insertion order is preserved
d) It can store duplicate values
e) In python, we use []
f) e.g. name_of_student = ["Malthi","Aarti","Abhinav","Malthi"]

# Tuple
a) ordered collection of items ( the order in which data is stored)
b) Immutable ( once created can not be changed )
c) Insertion order is preserved
d) It can store duplicate values
e) In python, we use ()
f) e.g. name_of_student = ("Malthi","Aarti","Abhinav","Malthi")

# Set
a) un-ordered collection of items ( the order in which data is stored)
b) Mutable ( once created can be changed )
c) Insertion order is not preserved
d) It can not store duplicate values
e) In python, we use {}
f) e.g. name_of_student = {"Malthi","Aarti","Abhinav"}



# List methods/functions
name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi"]

# datatype check
print(type(name_of_students_list))
print(name_of_students_list)

# Display each elements/items form the list
print("Hello ! welcome ",name_of_students_list[0])
print("Hello ! welcome ",name_of_students_list[1])
print("Hello ! welcome ",name_of_students_list[2])
print("Hello ! welcome ",name_of_students_list[3])

# using for loop
name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi"]
# range(0,4,1) equailvalent range(4)
# range(1,10,2) => 1,3,5,7,9
# Way 1:
for idx in range(0,4,1):
    print("Hello ! welcome ",idx,":",name_of_students_list[idx])


# Way2 :


for item in name_of_students_list:
    print(item)

# Add "Rakesh" in the list
name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi"]
print("Before adding Rakesh .....",name_of_students_list)
name_of_students_list.append("Rakesh")
print("After adding Rakesh.....",name_of_students_list)

# remove "Aarti" from list

print("Before removing Aarti .....",name_of_students_list)
name_of_students_list.remove("Aarti")
print("After adding Aarti.....",name_of_students_list)


# List slicing

name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi","Rakesh","Thomas","Pankaj"]

# Get me first 3 items from list and store in another list ( idx : 0,1,2 )
# way 1
ans_list = []
for idx in range(0,3,1):
    ans_list.append(name_of_students_list[idx])
print(ans_list)

# way 2 list slicing ( similar to range( startindex, endIndex, steps )
# syntax : list_name[startIndex:endIndex:steps]

print("Using slicing operator ",name_of_students_list[0:3:1])


# Tuple

name_of_students_tuple = ("Malthi","Aarti","Abhinav","Malthi")
print(type(name_of_students_tuple))

occurence_of_an_element = name_of_students_tuple.count("Malthi")

no_of_elements = len(name_of_students_tuple)
print(no_of_elements)



# Set

name_set1 = {"Ram","Shyam","Rakesh"}
name_set2 = {"Ram","Shyam","Ghanshyam"}

#print("Before : ", name_set1)
#name_set1.add("Shyam1")
#print("After : ", name_set1)

# Union
ans_set =  name_set1.union(name_set2)
print(ans_set)

# Interection
ans_set =  name_set1.intersection(name_set2)
print(ans_set)

# Difference
ans_set =  name_set1.difference(name_set2)
print(ans_set)

ans_set =  name_set2.difference(name_set1)
print(ans_set)


# symmetric Difference ( set1 - set 1 union  set2 - set1 )
ans_set =  name_set1.symmetric_difference(name_set2)
print(ans_set)
'''

# get me first 3  and last 3 elements  from the list

# first 3 elements will be at indexes = 0,1,2
# last 3 elements will be at indexes = n,n-1,n-3 (10,9, 8)

list_numbers = [1,2,3,4,5,6,7,8,9,10,"Akash"]

ans = []

first_list = list_numbers[0:3:1]
last_list = list_numbers[7::1]
print(first_list)
print(last_list)
ans = first_list+last_list
print("answer list : ",ans)
print("Before : ",list_numbers)
list_numbers[1] = 100
print("After : ", list_numbers)

