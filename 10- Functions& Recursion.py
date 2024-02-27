   
# FUNCTIONS   -----> Block Of a statement that performs a specific task
# the code which is repeted then we can use Functions 


def calc_sum(a, b):                                      # Here def is a keyword which means define
    sum = a + b
    print(sum)
    return sum

calc_sum(1,2)

calc_sum(33,22)   
calc_sum(30,52)


#  Another way


def sum_calc(c,d):     # (c,d) ----> these are parameters
    return c + d

summ = sum_calc(20,56)  #sum_calc() ----> this is function call
print(summ)             # (20,26) -----> this is arguments




def print_hello():
    print("hello")
    
print_hello()


# AVG of 3 numbers

def Avg_function(x, y,z):
    add = x+y+z
    avg = add/3
    print(avg)
    return avg

Avg_function(1,2,3)



    
# Functions in Python

# 1 -- Built In  Function

"""    

print()

len()

type()

range()


"""


# Default Parameters    ---> Assigning a default value to a parameter, which is used when no arguments is passed


def cal_pro(a =1,b=1):   # this is how we give the default value
    print(a+b)
    return a*b

cal_pro()



# PQ 1


ITEMS = ["SOAP", "BRUSH", "BOTTEL", "SHOE","CLOTHS"]

def len_fun(list):
    print(len(list))



def print_list(list):
    for items in list:
        print(items)
        
print_list(ITEMS)


# PQ 2


def cal_fact(N):
    fact = 1
    for i in range(1, N+1):
        fact *= i    
    print(fact)
        
cal_fact(6)


# PQ 3


def convert(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val,"INR")
    
convert(100)


# PQ 4

def odd_even(input):
    if (input %2 != 0):
        print("Input is ODD")
    else:
        print("Input is Even") 

odd_even(21)


#    RECURSION         ---->    When a function calls itself Frequently


def show(p):
    if (p == 20):    # ----> Base case --> it desides that the recursion should stop or not
        return
    print(p)
    show(p+1)       # Recursion
    
show(10)


# Call Stack  ---->  if we call a function and in that function we call same function many times is called call stack    


#        | p = 20 it matches|  when the condittion matches it deletes the stack and return to lower stack
#        |//////////////////|
#        |   |       |      |
#        |___|_______|______|
#        | p = 12, func 1   |  show(8)
#        |__________________|
#        | p = 11, func 2   |  show(9)
#        |__________________|
#        | p = 10, func 3   |  show(10)
#        |__________________|
#
#


# RECURSION  


def rec_func(L):
    if ( L == 0 or L == 1):
        return 1
    else:
        return  L * rec_func(L-1)
    
print(rec_func(5))
        
        
# PQ 1

def rec_sum(n):
    if(n == 0):
        return 0
    return rec_sum(n-1) + n

print(rec_sum(10))


hero = ["ironman", "superman", "captain america", "hulk"]


def list_func(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    list_func(list, idx+1)
    
list_func(hero)
    
