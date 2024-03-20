
# Polymorphism : Operator Overloading
# When the same operator is allowed to have diffrient meanings according to the context

print(1 + 2)  # 3
print("Tarun" + "Reddy") # concatination
print([1,2,3,] + [4,5,6]) # merge

"""   Operators & Dunder functions  (Double underscore)

a+b         #addition                  a__add__(b)

a-b         #subtraction               a__sub__(b)

a*b         #multiplication            a__mul__(b)

a/b         #division                  a.__truediv____ (b)

a%b         #addition                   a.__mod____(b)

"""

# complex numbers

class Complex:
    def __init__(self, Real, img):
        self.Real = Real
        self.img = img
        
    def showNum(self):
        print(self.Real, "i + ", self.img, "j")
        
    def __add__(self,  num2):                                 # here 
        newReal = self.Real +   num2.Real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)
        
        
num1 = Complex(1,3)
num1.showNum()

num2 = Complex(4,6)
num2.showNum()

#  num3 = num1.add(num2)
#  num3.showNum()

num4 = num1 + num2     #      For executing this we use __add__ (above  ^ )
#                                                                       | 
