'''
# Q1 : Given a list , find the count of each element in the list
# e.g. marks = [10,11,12,13,15,10,20,12,15,12}
# O/p = 10 : 2, 11 : 1,12: 3, 13: 1,15: 2

def count_marks_occurence(list1):
    count_dict ={10:2}
    for ele in list1:
        if ele in count_dict:
           count_dict[ele]= count_dict[ele] + 1
                            # count_dict[10] = 1 +1=2
        else:
            count_dict[ele] = 1
            #  count_dict[10] = 1
    return count_dict


marks = [10,11,12,13,15,10,20,12,15,12]
ans_dict = count_marks_occurence(marks)
print(ans_dict)

# Q2 Find all the duplicate marks in the list and return a list

def getDuplicateMarks(ans_dict):
    duplicate_lst = []
    for key in ans_dict.keys():
        if ans_dict[key] > 1:
            duplicate_lst.append(key)

    return duplicate_lst

ans_list = getDuplicateMarks(ans_dict)
print(ans_list)

# Q3 Find all the uniquely occured marks in the list and return a list

def getUniqueMarks(ans_dict):
    unique_lst = []
    for key in ans_dict.keys():
        if ans_dict[key] == 1:
            unique_lst.append(key)

    return unique_lst

ans_list = getUniqueMarks(ans_dict)
print(ans_list)


# Q4 Find all the unique and duplicate marks from  the list and return in seperate lists
def getDuplicateMarks(ans_dict):
    duplicate_lst = []
    unique_lst = []
    for key in ans_dict.keys():
        if ans_dict[key] > 1:
            duplicate_lst.append(key)
        else:
            unique_lst.append(key)

    return duplicate_lst,unique_lst

ans_list = getDuplicateMarks(ans_dict)
print("Duplicate lists : ",ans_list[0])
print("Unique lists : ",ans_list[1])




# String Slicing
city = "Bangalore"

# first 4 character
# way 1 :
for idx in range(0,4,1):
     print(city[idx],end=" ")

print()
# Way 2 using slicing
print(city[0:4:1])

# Print every even indexed charcters ( 0,2,4,6,....)
print(city[0::2])

# Print every odd indexed charcters ( 1,3,5,7,....)
print(city[1::2])


city = "Bangalore"
# Print last 4 charcter in the city name
print(city[-1],end= "")
print(city[-2],end= "")
print(city[-3],end= "")
print(city[-4],end= "")
print()

print(city[-1:-5:-1])

print(city[3:0:-1])

# print the whole string in reverse
print(city[::-1])


# split
email = "etlqalabs@gmail.com"
lst1 = email.split("@")
print(lst1[0])
print(lst1[1])

name = "Akshay Ranjal"
name_list = name.split(" ")
print("first name : ",name_list[0])
print("last name : ",name_list[1])



# Doubt session

name = "etlqa@gmail.com"
l1 =  name.split("@")
print(l1)
l2 = l1[1].split(".")
print(l2)

'''


# Replace a specific character in a string ( 1 occurence with 1 , 2nd wth 2 .....)
name = "akshay Ranjal"
# o/p = "1ksh2y R3nj4l"
ans_name = ""
start_num = 1
size = len(name)
print(size)
for i in range(size):
    if name[i] =='a':
        ans_name = ans_name+str(start_num)
        start_num =  start_num +1
        print(ans_name)
    else:
        ans_name = ans_name+name[i]
        print(ans_name)


print(ans_name)




