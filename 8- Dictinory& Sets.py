# Dictionary are used to store data values in ( KEY : VALUE ) pairs
# They are UNORDERED , MUTABLE and do not allow Duplicate keys


info = {
    # "KEY"   : "Values"
    "name" : "tarun",
    "age" : 23,
    "subjects" : ["python", "HTML", "CSS" , "JS"],
    "marks" : 99.9,
     "pass" : True
}
print(info)
print(info["name"])
print(info["age"])
print(info["subjects"])

info["name"] = "Tarun reddy "   # by this the value will be changed which is present in name key
print(info)

info["surname"] = "str"          # It add the new key to the dictionary
print(info)


null_dict = {}                   # creates the null dict
print(null_dict)                 # we can add the values to the null_dict if we need

# NESTED DICTIONARIES  ----> we can turn the value to the dictionary

student = {
    "name" : "reddy",
    "marks" : {
        "physics" : 52,
        "chem" : 68,
        "maths" :99
    }
}

print(student)
print(student["marks"])
print(student["marks"]["chem"])   # Prints the value which is present




                                         # DICT METHODS


#  my.Dict.keys        ----> Returns all the keys
#  my.Dict.values      ----> Returns all the values
#  my.Dict.items       ----> Returns all (key, value) pair as tuple
#  my.Dict.get("key")  ----> Returns the key according to the value
#  my.Dict.update      ----> R
#  my.Dict.


print(student.keys())
print(list(student.keys()))    # it changes the dict to list

print(student.values())
print(list(student.keys()))


print(student.items())  # it gives the value in pairs Ex :- (name : reddy) ( marks : physics)
pairs = list(student.items())
print(pairs[0])


print(student.get("name"))
print(student.get("name2"))  # -- None
# print(student("name2"))    # -- Error

                               
student.update({"city" : "hyd", "age" : 33, "name" : "TARUNREDDY" })
print(student)









#                                                     SET in Python


# set is a collection of unordered items  (no index)
# each element in a set must be unique & immutable
# Ex:- set = {1,2,3,3,3,2,1,4} ----> The repeted elements will be stored once, so it will be resolved as {1,2,3,4}


collection = { 5,58,6,8,4,4}
print(collection)
print(type(collection))
print(len(collection))


coll = set()  # --> Empty set
print(type(coll))




#    SET METHODS 

#  set.add(element)         --> adds the element
#  set.remove(element)      --> removes the element
#  set.clear()              --> make the set empty
#  set.pop()                --> removes a random value
#  set.union(set2)          --> combines both set values and returns new
#  set.intersection(set2)   --> combines common values and returns new


#    SET are  mutable  -- but -- Elements present in the SET are immutable

collection.add(1)
collection.add(2)
collection.add("REDDY")
collection.add((33,44,55))
print(collection)


collection.remove(58)
print(collection)


print(len(collection))

#collection.clear()
print(len(collection))


print(collection.pop())



set1 = {1,2,3,4,5,66,77}
set2 = {1,2,33,44,55,66,77}

print(set1.union(set2))

print(set1.intersection(set2))



# PQ-1

word = {
    "table" : ["a piece of wood","list of facts and figures"],
    "cat"   : "a small animal"
}

print(word)