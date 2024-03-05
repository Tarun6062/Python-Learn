# Python is a Indentation language (Four spaces is required after :)


# In conditional statement there is a condition while executing the program    
# if-elif-else

age = 22                  
if( age >= 29):                           # it gives the Condition
    print("You are Eligible")
elif(age < 20):                           # when if condition fails it executes this condition
    print("Underage")
else:                                     # when both if and elif condition fails then this will execute
    print("you are not eligible")
    

# another Example of conditional statement

light = input("Light :")
if(light == "red"):
    print("stop")
elif(light == "orange"):
    print("ready")
elif(light == "green"):
    print("start")
else:
    print("The signal is broken")

# Marks Example

marks = int(input("marks :"))
if( marks >= 90):
    print("you scored A")
elif(marks >=70 and marks < 90):
    print("you scored B")
elif(marks >=50 and marks < 70):
    print("you scored C")
elif(marks >=40 and marks < 50):
    print("you scored D")
elif(marks >=30 and marks < 40):
    print("you scored E")
else:
    print("You are failed")
    


#     TERNARY Operator
#   Ex:-  <var> = <val1> if(condition) else(val2)

food = input("food :")
eat = "YES" if food == "apple" else  "no"
print(eat)

# <statement1> if(condition) else <statement2>

games = input("Enter the game name :")
print("Outdoor Game") if games == "football" or games == "cricket" else("It is not a outdoor game")



# clever If / Ternary operator
# <var> = (false_val , true_val) [condition]

age = int(input("age :"))
vote = ("yes","no") [age <= 18]
print(vote)

