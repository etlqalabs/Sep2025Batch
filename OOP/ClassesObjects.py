class Display:
    name = "ETL QA Labs"
    def print_number(self,num):
        for i in range(num+1):
            print(i)

# Create an object
obj1 = Display()
#print(obj1.name)
#obj1.print_number(10)
# address of the the object
print(id(obj1))



obj2 = Display()
#print(obj2.name)
#obj2.print_number(20)
# address of the the object
print(id(obj2))
