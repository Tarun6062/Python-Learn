
#             == == == == == == == == == == == ==   Practice Questions == == == == == == == == == == == == ==

# PQ-1

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self ):
        return 2 * (22/7) * self.radius
    
            
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# ========================================================= X =====================================================


# PQ-2

class Employee:
    def __init__(self , role , dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role :-" , self.role)
        print("Dept :-" , self.dept)
        print("salary :-" , self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000") 
        
e1 = Employee("Accountant" , "Finance", 20000)
e2 = Employee("Developer" , "IT", 200000)

print(e1.showDetails())

eng1 = Engineer("ElonMusk", 40)

eng1.showDetails()

# ========================================================= X ====================================================

# PQ-3

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, o2):
        return self.price > o2.price
        

o1 = Order("Apple", 100)
o2 = Order("Banana", 60)
        
        
print(o1 > o2)
        
