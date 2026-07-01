# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# class employee:
   
#     language = "Python"
#     salary = 50000

# harry = employee()
# print(harry.salary)


#self is a reference to the current instance of the class. It is used to access variables that belong to the class.

class Student:
    language = "Python"
    marks = 80

    def getInfo(self):
        print(f"Language: {self.language}, Marks: {self.marks}")

# Create an instance of the Student class
student1 = Student()
student1.getInfo()