#***************************************
#List, a list store sequences of items

"""a = [1,2,3] #Create a new list with three items
a.append(4) #Add stuff to the end of the list
a.append(5)
a.pop() #Remove the last item
print(a) #Print the complete list
print(a[0]) #Print the first item of list
print(a[-1]) #Print the last item of list
print(a[0:2]) #Slice syntax, a[start:end:step]
print(a[2:]) 
print(a[:3]) 
print(a[::2]) 
print(a[::-1]) 
b = a[:] #Copia de toda la lista a en b
print(b)
del a[2]  #Remove the item in the 2 index 
a.remove(4) #Remove the first occurrence of the value 4 in a
print(a) #Print the complete list
print(a+b) #The sum of both lists
a.extend(b)  
print(a)
print(4 in a) #Check for existence in list a
print(len(a)) #Length of list a """

#***************************************
#Tuple, like list but inmutable (just one type of data each time)
"""a = (1,2,3) #Create a new tuple
print(a[0]) #Print the first item
print(type(1)) #Knowing the type of number 1
print(len(a)) #Length of tuple a 
b = (4,5,6) 
a = a+b
print(a) #The sum of both tuples
print(a[:4]) #Slice syntax

# Unpack tuples and lists into variables
a, b, c = (1, 2, 3)  # a is 1, b is 2 and c is 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is 1, b is [2, 3] and c is 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e = 5 and f = 6
e, d = d, e  # Swap two values"""

#***************************************
#Dictionaries, store mappings from keys to values
# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
"""a = {"one": 1, "two": 2, "three": 3}
b = {(1,2,3):[1,2,3]} #Values can be of any type
print(list(a.keys())) #Get all keys as an iterable with keys()
print(list(a.values())) #Get all values as an iterable with values()
print("one" in a) #Looking for a key "one"
print(a.get("one")) #Get value of the key given
print(a.setdefault("five", 5)) #Get the value given if is not present 
a.update({"six": 6}) #Adding to a dictionary
a["four"] = 4 
del a["one"]  # Removes the key "one" from dict
print(a)"""

#***************************************
#Sets
"""a = set()
a = {1, 1, 2, 2, 3, 4}  #New set 
a.add(5)  #Add a new value
b = {3, 4, 5, 6}
print(a & b) #Intersection
print(a | b) #Union
print(a - b) #Difference
print(a ^ b) #Symmetric
print(a >= b) #Check if set on the left is a superset of set on the right
print({1, 2} <= {1, 2, 3}) #Check if set on the left is a subset of set on the right
print(2 in a) #Check existence of values in sets
c = b.copy()  #Make a copy of b to c"""

#***************************************
#Lambda, or annonymous functions
"""print((lambda x: x > 2)(3))
a = []
print(list(map(lambda x: x + 2, [1, 2, 3])))
print(list(map(max, [1, 2, 3], [4, 2, 1]))) 
print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))"""

#***************************************
#Built in functions (datetime)
"""import datetime 
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%B")) 
print(x.strftime("%d"))"""

#***************************************
#Decorators, change the behaviour of a function 

#1
def upper(text):
    return text.upper()

print(upper("Hello"))
again = upper # <-- Decorator
print(again("Hello"))

#2
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    greeting = func("""Hi there""") # <-- Decorator 
    print (greeting)
 
greet(shout)
greet(whisper)
