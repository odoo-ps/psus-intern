# make a function that generates fibonacci numbers
# fibonacci numbers are the numbers in the following sequence:
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# store the first 100 finbonacci numbers in a list
fibonacci_list = []
for i in range(10):
    fibonacci_list.append(fibonacci(i))
# plot fibonacci_list
import matplotlib.pyplot as plt
plt.plot(fibonacci_list)
plt.show()