   

# Class Attributes

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
