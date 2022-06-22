#lambda arguments:expression (only one expression allowed)
#1
"""
    Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
    also create a lambda function that multiplies argument x with argument y and print the result. 
"""
addFiftheen=lambda a:a+15
multiply=lambda x,y:x*y

num=addFiftheen(10)
print(num)
num=multiply(num,15)
print(num)
#2
"""
    Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]   
"""
unsorted_cars=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(unsorted_cars)
#sorted() sorts list and tuple, return a list with sorted elements.
#key in sorted(), key=lowercase--->
sorted_cars=sorted(unsorted_cars,key=lambda x:x['make'])
print("after sorting by make")
print(sorted_cars)

#3
"""
    Write a Python program to filter a list of integers using Lambda. 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""
#fliter() function takes two arguments: function, sequence
old_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#using list() to get a list from fliter
even_numbers=list(filter(lambda x:x%2==0,old_list))
print(even_numbers)
odd_numbers=list(filter(lambda x:x%2!=0,old_list))
print(odd_numbers)
#4
"""
    Write a Python program to find if a given string starts with a given character using Lambda
"""
given_string='helloworlds'

is_start_with=lambda x,list:x==list[0]
print(is_start_with('c',given_string))
print(is_start_with('h',given_string))
#second solution

#given character with input string
starts_with=lambda x:True if x.startswith('P') else False
print(starts_with("Pheghg"))
print(starts_with("xheghg"))

#5
"""
    Write a Python program to find the elements of a given list of strings that contain specific 
substring using lambda
"""
list_of_strings=['red', 'black', 'white', 'green', 'orange']

def search_substring(list_of_strings,substring):
    return list(filter(lambda x:substring in x,list_of_strings))

print(search_substring(list_of_strings,'ack'))

