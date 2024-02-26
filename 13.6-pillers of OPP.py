


# Abstraction

# Hiding the implementation details of a class and showing the essential features to the user

class Car:                              # from  Here 
    def __init__(self):
        self.acc =  False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("car Started")           #  To Here  is called Abstraction
        
c1 = Car()
c1.start()


# Encapsulation   

# Wrapping DATA and FUNCTION in a single unit is called Encapsulation







# PQ1

class Account:
    def __init__(self , accountNo , balance):
        self.account = accountNo
        self.balance = balance

    

    
    # Debit
    def debit(self , Amount):
        self.balance =- Amount 
        print("Rs ", Amount , " Was Debited")
        print(" Total balance", self.get_balance())
        
    # Credit
    def credit(self, Amount):
        self.balance += Amount
        print("Rs ", Amount ," Was credited" )
        print(" Total balance", self.get_balance())
       
        
    # Balance
    
    def get_balance(self):
        return self.balance
        
A1 = Account(1545447, 5000)
A1.debit(777)
A1.credit(777777777)









        
    
        
    
