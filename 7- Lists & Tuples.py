# LISTS --> It is a built in data type which stores set of values
# It can store elements of different types (int, string, float etc)
     
marks = [45.2,55,11,22,66,8,9,99]
print(marks)
print(type(marks))

print(marks[0])
print(marks[5])
print(len(marks))  # lists can store different type of data 
                   # But array can only store same type of data

students = ["reddy", 54, 66,45,55,"tarun"]    # list are mutable
print(students)                               # strings --> immutable


                                                          # List Slicing


# Ex : -- list_name[ start_idx : ending_idx ]   (note:- the ending index will be not executed)


#        0  1  2  3  4  5
Marks = [12,55,23,65,85,44]
#        -6 -5 -4 -3 -2  -1

print(Marks[2:5])

# marks[1:4] -- [55,23,65]
# marks[ :4] -- [55,23,65]
# marks[1: ] -- [55,23,65,85,44]
# marks[-3:-1]- [65,85]
print(Marks[-3:-1])

                                                           # List Methods
"""
1 ----list.append(4)    
2 ----list.sort()
3 ----list.sort(reverse=True)
4 ----list.reverse()
5 ----list.insert(idx, element)
6 ----list.remove(element)
7 ----list.pop(idx)
"""


list = [2,1,6,7,9,4]
list.append(5)            # 1 -- Append (adds one element at the end)
print(list)

list.sort()               # 2 -- Sort (sorts the list in ascending order)
print(list)

list.sort(reverse=True)   # 3 -- Sort(reverse=True) (sorts in decending order)
print(list)

list.reverse()            # 4 -- Reverse (reverses the list)
print(list)               

list.insert(2, "hello")   # 5 -- Insert (insert element at index)
print(list)

list.remove(6)            # 5 -- removes the first occurence of the element
print(list)

list.pop(2)               # 7 -- removes element at index
print(list)



                                                      # TUPLE

# The built in data type that creates immutable sequence of values

tup = (22,33,44,55,66,33,33,77)  # we use () in tuple
print(tup.index(22)) 
print(type(tup))


tup1 = ()  # it is valid empty tuple
print(tup1)
print(type(tup1))

# tuple methods

print(tup.index(22))  # returns index of the first occurance
print(tup.count(33))  # counts how many times the element is present in tuple




# Practice question 1

m1 = input("enter your 1st fav movie :-")
m2 = input("enter your 2nd fav movie :-")
m3 = input("enter your 3rd fav movie :-")

movies = [m1, m2, m3]
print(movies)

# Practice question 2

L1 = [1,2,3,2,1]
L2 = [1,2,3,4,1]

cl1 = L1.copy()
cl1.reverse()

if(L1 == cl1):
    print("Palindrome")
else:
    print("not a Palindrome")
    
cl2 = L2.copy()
cl2.reverse()

if(L2 == cl2):
    print("Palindrome")
else:
    print("not a Palindrome")


# problem question 3

A = ("C","D","A", "A", "B","B","A")
B = A.count("A")
print(B)

# P4

a = ["C","D","A", "A", "B","B","A"]
a.sort()
print(a)
