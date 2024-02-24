# Loops are used to instruction

# While Loop

count = 1
while count <= 5  :
    print("hello")
    count = count + 1
   
print(count)

"""
# For printing from 1 to 199
i = 1 
while i <= 199 :
    print("yoo bro", i)    # this is used for the string
    i += 1
    
print("Loop ended")  """

                                                                     # #  # # # # # # # # # # # # # # # #

"""

# For printing from 20 to 1

j = 20
while j >= 1:
    print("bye", j)
    j -= 1
    
print("done")


# PQ 1

# Print numbers from ! to 100

k = 1 
while k <= 100:   
    print(k)
    k += 1


# Multiplication of the given number

n = int(input("enter the number :-"))
y = 1
while y <=10:
    print( n * y )
    y += 1


# PQ 3

No = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(No):
    print(No[idx])  # By this method we can get the values by index
    idx += 1



# PQ 4

El = (1,4,9,16,25,36,49,64,81,100)

f = 49
z = 0
while z < len(El):
    if(El[z] == f):
        print("found at index ", z)
    else:
        print("Not available")
    z += 1




#                                                            BREAK & CONTINUE


# BREAK --> Used to teremenate the LOOP when encounter


i = 1
while i <= 10:
    print(i)
    if (i == 5):
        break               # This key word breaks the loop at 5 and it will not execute the others Elements
    i += 1
    
    print("end of loop")

# CONTINUE  ---> Terminates execution in the current iteration & continue execution of the loop with the next iteration 





p = 0
while p <= 5:
    if(p == 3):
        p += 1
        continue       #  Continue ( SKIP )keyword does not print the 3 and prints all the elements except 3
    print(p)
    p += 1
    
    
# PQ 1 

# Printing ODD numbers from 1 to 20


v = 0
while v <= 20:
    if(v%2 == 0):
        v += 1
        continue
    print(v)
    v += 1
    
    
# Printing EVEN numbers from 1 to 20


l = 0
while l <= 20:
    if(l %2 != 0):
        l += 1
        continue
    print(l)
    l += 1
    
#                                                       FOR LOOPS

# For loops are used for sequential Traversal.  For traversing List, Tuple, String etc. 


items = ["box", "key", "lock", "mobile"]

for val  in items:
    print(val)
    
    
    
A = [1,4,9,16,25,36,49,64,81,100]

x = 25

idxx = 0

for el in A:
    if(el == x):
        print("no found at", idxx)
    idxx += 1



"""

#                                                            RANGE in Loops


# Range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (By default ), and stops before a specified number

# range(start?,stop, step?)




for rg in range(2, 10):   # Here 10 is the stop condition   
    print(rg)             # 2 is the star condition
                          # 
    
    
for i in range(1, 10 , 2):   # Here 10 is the stop condition    # 1 is start  # 2 is the step which means it will increace by 2
    print(i)             
                          
    



# LINEAR SEARCH   - - - - - >   It means searching a value in a sequencial way 


# PQ 1

for j in range(100, 0, -1):
    print(j)


# PQ 2

q = int(input("Enter the number :-"))

for t in range(1, 11):
    print(q * t)
    
    
# Pass Statement     ----> It is a null statement that does nothing. It is used as a placeholder For future code

for el in range(10):
    pass                    # this statement does not execute the loop

print("yo")



# PQ 1


n = 5

sum = 0
for f in range (1,n+1):
    sum += f
    
print(sum)



# PQ - Factorial

p = 5

fact = 1
r = 1

while r <= p:
    fact *= r
    r += 1
    
print("factorial of n is:-", fact)
