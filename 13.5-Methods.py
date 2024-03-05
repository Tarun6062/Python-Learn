    

# Methods  --> These are the functions that belongs to object



#                           [ Class ]
#                           ____|___        
#                          /        \
#                         /          \
#                        /            \
#                   DATA                METHODS
#             (attributes)              (functions)
#      (ex:- Properties of car)            (ex:- how does it run)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("your avg score is ", sum/3)
        
s1  = Student("tony", [88,99,77])

s1.avg()
    



# Static methods

class Collage():
    @staticmethod                # Decorators  ---> it changes the behaviour of the givrn function
    def hello():
        print("hello")
        
s1 = Collage()

s1.hello()




