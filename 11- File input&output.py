# FILE I/O
                    
# Python can be used to perform operation on a file .( READ & Write data)
         
# TYPES OF FILES

# 1 -- TEXT FILE  ---:> Data which is stored in characters form
#             EX :-       .txt, .docs,  .log

# @ -- Binary Files ---:>    


#  "r"    --->  open for reading (deafult)
#  "w"    --->  open for writing, truncating the file first
#  "x"    --->  create a new file and open it for writing
#  "a"    --->  open it for writing, appending to the end of the file if it exists
#  "b"    --->  binary mode
#  "t"    --->  text mode  (default)
#  "+"    --->  open a disk file for updating (reading and writing)


f = open("12-demo.txt","r")

# READING A FILE

data = f.read(5)
print(data)
print(type(data))

line1 = f.readline()
print(line1)


# WRITING A FILE

# w   -->  Over write
# a   -->  Add at the end


f = open("12-demo.txt","a")
data = f.write(" /n good morning boysss")



"""
with open("demo1.txt", "r") as f:   # Here as is known as alias
    data = f.read()
    print(data)
    
    """

    
    
# DELETING A FILE

# using this OS module --> Module (like a code library)  is a file written by another programmer that generally has a function we can use



# PQ 1

with open("practice.txt", "r") as f:
   data = f.read()
   
new_data = data.replace("Java", "python")
print(new_data)

# PQ 2

with open("practice.txt", "w") as f:
    f.write(new_data)
    
# PQ 3

def check_func():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
            
check_func()

    
    
    
