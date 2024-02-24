# STRINGS
# String is a datatype that stores a sequence of characters
    
str1 = "my name is tarun /n i am 22 years old" # here /n is a ESCAPE SEQUENCE CHARACTER which send the sentence to next line

# Concatination

str2 = "hello"
str3 = "world"
sum = str2 + str3 # concatination means we can add two strings
print(sum)
print(len(str2))  # prints the length of the string

# INDEXING  -> It helps to access the characters

#  T A R U N R E D D Y
#  0 1 2 3 4 5 6 7 8 9

str = "TARUNREDDY"
ch = str[5]  
print(ch)    # --> we can only access the characters with indexing we cannot manupulate them
 
 
# Slicing  -> Slicing is used to access the parts of string

#  Str [starting_idx : ending_idx] in this the ending will not be printed

str4 = "tarunreddy"
print(str4[0:5])  # [:5] we can also write like this


# String Function
""" srt = 'I am a coder'

str.endswith("er.")      # returns TRUE if it really ends with er

str.capitalize()         # makes the first letter capital

str.replace(old,new)     # replaces all old characters with new characters

str.find(word)           # finds the word at what index it is at

str.count("am")          # counts the word how many times it occured

"""

# practice question 1

str5 = input("enter your name :")
print("length of your string is :", len(str5))

# practice question 2

STR = "Hi, $sn $ojdnf $ doign $ sfin"
print(STR.count("$"))

# Conditional statement


age = 14 

if(age >= 18):
    print("you can vote")
else:
    print("you cannot vote")
    
# NESTING  --> Nesting means writing one statement in another statement


age2 = 30

if(age2 >= 18):
    if(age2 >=80):
        print("cannot drive")  # it is a  Valid code 
    else:
        print("can Drive")
else:
    print("cannot drive")
    

# Practice question 2

# ODD OR EVEN

num = int(input(" Enter the number"))
if(num % 2 == 0):
    print("It is a even number")
else:
    print("It is a odd number")
    
# Practice question 3

# Greatest of 3 numbers

num1 = int(input(" Enter the first number"))
num2 = int(input(" Enter the second number"))
num3 = int(input(" Enter the  third number"))

if (num1 > num2 and num1 > num3):
    print("Num1 is the greatest number : ")
elif(num2 > num1 and num2 > num3):
    print("Num2 is the greatest number : ")
elif(num3 > num1 and num3 > num2):
    print("num3 is the greatest number : ")


# Practice question 4

NUM1 = int(input(" Enter the 1st number "))


if(NUM1 % 7 == 0):
    print("It is a Multiple of 7")
else:
    print("it is a not a multiple of 7")
