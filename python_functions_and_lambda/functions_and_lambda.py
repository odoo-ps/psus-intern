"""
Write a Python function that takes a list
 and returns a new list with unique elements of the first list.
 Go to the editor
 Sample List : [1,2,3,3,3,3,4,5]
 Unique List : [1, 2, 3, 4, 5]
"""



def filter_values(list_values):
    """_summary_

    Args:
        list of values
    """
    unique_values = []
    for item in list_values:
        if not item in unique_values:
            unique_values.append(item)               
    return unique_values
values = [10,2,2,2,3,3,3,4,4,5,67,8,9]

print(filter_values(values))
#########          LAMBDA   ##########################
# Write a Python program to create a lambda function that adds 15 to
# a given number passed in as an argument, also create a lambda function
# that multiplies argument x with argument y and print the result.

add15 = lambda x: x+15
multilplies = lambda x,y: x*y


print(add15(5))
print(multilplies(5,5))


#Write a Python program to create a function that takes one argument,
#and that argument will be multiplied with an unknown given number.
def multilicator(n):
    return lambda x: x*n
result = multilicator(2)
print("Double the number of 15 =", result(15))

#Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#Sorting the List of Tuples:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

sort_tuple_list = lambda mylist: mylist[1]

#Using .sort() method, create a lambda function that sorts
#the list in descending order.

lst=[100, 10, 10000, 1, 9, 999, 99]
lst.sort(key=lambda x: 100/x)
print(lst)
