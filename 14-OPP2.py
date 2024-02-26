
#  del keyword    ----> used to delete object properties or object itself

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Tarun0")
print(s1.name)    
#del s1.name      # deletes the object property


# Private(like)   attribute and methods

# ---> private attributes & methods are ment to used within the class and not accessible from out side the class


class Account:
    def __init__(self, acc_no , acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

