# Constructor   --> A Constructor is a special method in a class used to create and initialize an object of a class
# Constructor   --> A Constructor is a unique function thats gets called automatically when an object is created  of a class
     
class Person:        
#   name = " REDDY"
#   occ = "Deops"
    def __init__(self, n , o):    # parametarized constructor
        print("hey i am a person") 
        self.name = n
        self.occ = o 
    
    def info(self):
        print(self.name, "is a", self.occ)
        
a = Person("Reddy", "Developer")
b = Person("Kumu", "HR")
a.info()
b.info()

#a.name = "Thor"
#a.occ = "God"   
#a.info()


Note = "THERE ARE TWO TYPES OF CONSTRUCTORS"

# Parameterized Constructors  --> When a constructors accepts aruguments along with self is known as Parameterized Constructors
# Default Constructors        --> Doesn't accept any arguments and has only one argument (self) is known as Default Constructors


class Collage:
    Collage_name = "YOO"
    name = "nothing"         # Class attribute
    
    def __init__(self, name, age):
        self.name = name     # object attribute >  Class attribute
        self.age = age
        print("your name is", self.name ," and your age is " ,self.age)
        
        
s1 = Collage("kume", 20)
s2 = Collage("tarun" , 24)
s3 = Collage("midhun", 99)

print(s1.Collage_name)
print(s2.Collage_name)
print(s3.Collage_name)
