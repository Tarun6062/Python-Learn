class Person:
    name  = "REDDY"
    occup = "Developer"
    age   = 22
    def info(self):     # Self  parameter is a reference to the current instance of the class, and it is used to access variables that belongs to the class
        print(self.name, "is a ", self.occup, " and he is ", self.age, "years old")
        
a = Person()
b = Person()
a.name = "Tarun"
a.occup = "Software developer"

b.name = "kumu"
b.occup = "HR"  

a.info() 
b.info()
  

  
   
   
   
