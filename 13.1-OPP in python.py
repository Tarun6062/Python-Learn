                             
#  OPP IN PYTHON 
   
# to map with real world scenarioes, we started objects in code this is called Object oriented programming
 

# CLASS    ---> class is a blueprint for creating objects
 
class Student:    # The name of the class should start with capital letter
     name = "tarun"
    
# Object (instance) is variables that contain data and functions that can be used to manipulate the data.

s1 = Student()   # This is a object
print(s1.name)

s2 = Student()
print(s2.name)

class Car:
    color = "Blue"
    brand = "Benz"
    def __init__(self, fullname):
        self.name = fullname
        print("new car")
    
c1 = Car("ford")
print(c1.name)

c2 = Car("BMW")
print(c2.name)
# __init__ function 

# Constructor   ---->  All classes have function called __init__(), which is always executer when the object is  being initiated
